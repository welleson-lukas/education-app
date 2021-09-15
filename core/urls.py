from django.urls import path
from core.views.usuario_views import teste
from core.views.post_views import PostView
from core.views.author_views import MyProfileView, MyProfileData

urlpatterns = [
    path('', teste, name='teste'),
    path('my/', MyProfileView.as_view(), name='MyProfileView'),
    path('my-data/', MyProfileData.as_view(), name='MyProfileData'),
    path('publicacao/<slug>/', PostView.as_view(), name='PostView'),
]