from django.shortcuts import render
from rest_framework import mixins, viewsets, generics, filters, pagination
from rest_framework.response import Response

from .models import Story, User
from . import BaseView
from rest_framework_extensions.cache.decorators import cache_response


class StoryView(mixins.ListModelMixin, BaseView):

    queryset = Story.objects

    @cache_response(60 * 1, cache ='default')
    def list(self, request):
        User.objects.create(**{"username": '冯武鹏', 'avatar': 'https://api.png'})
        return Response({'ok': "很好！"})


class UserView(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = User.objects.all()

    def list(self, request):
        pass


class User1View(BaseView):

    def get(self, request):
        pass