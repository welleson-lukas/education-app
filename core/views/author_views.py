from django.http import JsonResponse
from django.views.generic import TemplateView, View
from core.models.author import Author


class MyProfileView(TemplateView):
    template_name = 'core/my_profile.html'


class MyProfileData(View):
    def get(self, *args, **kwargs):
        profile = Author.objects.get(user=self.request.user)
        qs = profile.get_sugestion_for_following()

        profile_to_follow_list = []
        for user in qs:
            p = Author.objects.get(user__username=user.username)
            profile_item = {
                'id': p.id,
                'user': p.user.username,
                'image': p.image.url
            }
            profile_to_follow_list.append(profile_item)

        return JsonResponse({'sf_data': profile_to_follow_list})