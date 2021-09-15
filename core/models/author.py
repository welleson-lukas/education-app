import uuid
import os
import random

from PIL import Image
from django.utils.text import slugify
from django.conf import settings

from itertools import chain
from django.db import models
from django.contrib.auth.models import User


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("avatar", filename)


class Author(models.Model):
    image = models.ImageField('Avatar', upload_to=get_file_path, default='avatar.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='authors')
    slug = models.SlugField('Slug', max_length=254, null=True, blank=True, unique=True)

    about = models.TextField('Sobre o Autor', max_length=500, null=True, blank=True)

    facebook = models.CharField('Facebook', max_length=255, null=True, blank=True)
    linkedin = models.CharField('Linkedin', max_length=255, null=True, blank=True)
    twitter = models.CharField('Twitter', max_length=255, null=True, blank=True)
    github = models.CharField('Github', max_length=255, null=True, blank=True)

    following = models.ManyToManyField(User, related_name='following', blank=True)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    @staticmethod
    def resize_image(img, new_width=600):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.user.username)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 600

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.user.username

    def get_my_posts(self):
        return self.post_author.all()

    @property
    def num_posts(self):
        return self.post_author.all().count()

    def get_following(self):
        return self.following.all()

    def get_following_users(self):
        following_list = [p for p in self.get_following()]
        return following_list

    def get_my_and_following_posts(self):
        '''
        1) get the list of users that are following us
        2) initialize an empty posts list and set qs equal to none
        3) loop through the users list
        3A) for each user that we are following - grab it's profile
        3B) for every profile that we know have - grab the posts
        3C) add the posts to the post list
        4) grab our posts
        5) if posts list isn't empty sort the posts by created date
        '''
        users = [user for user in self.get_following()]
        posts = []
        qs = None
        for u in users:
            p = Author.objects.get(user=u)
            p_posts = p.post_author.all()
            posts.append(p_posts)
        my_posts = self.post_author.all()
        posts.append(my_posts)
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created_at)
        return qs

    def get_sugestion_for_following(self):
        '''
        1) get the profiles excluding our own
        2) create the followers list for our profile
        3) create and available list where:
            - we loop through the profiles
            - next we check if a particular profile is not on the followers list
            - only then we add that profile to the available list
        4) we shuffle the available list
        5) we return 3 first items of the available list
        '''
        profiles = Author.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_following()]
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]

    @property
    def following_count(self):
        return self.get_following().count()

    def get_followers(self):
        '''
        1) Create a queryset of all profiles
        2) create an empty followers list
        3) loop through the profiles
        4) perform and if statement to check if a single profile has us on the following list
        5) if the if check is true - add this profile to the followers list
        '''
        qs = Author.objects.all()
        followers_list = []
        for profile in qs:
            if self.user in profile.get_following():
                followers_list.append(profile)
        return followers_list

    @property
    def followers_count(self):
        return len(self.get_followers())
