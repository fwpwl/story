"""
the story api urls 
use django rest framework router 
"""
from django.conf.urls import url
from rest_framework import routers

from .views import UserView, StoryView, User1View


# router = routers.SimpleRouter()
# router.register(r'story', StoryView)
# router.register(r'user', UserView)

urlpatterns = [
    url(r'^api/v1$', User1View.as_view()),
]
# print(router.urls)
# urlpatterns += router.urls