from django.contrib.auth.models import Group, Permission
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from api.authentications import MyAuth
from api.models import User
from api.permissions import MyPermission
from api.throttle import SendMessageRate
from utils.response import APIResponse


class TestAPIView(APIView):
    authentication_classes = [MyAuth]
    def get(self, request, *args, **kwargs):
        user=User.objects.first()
        # print(user)
        # print(user.groups.first())
        # print(user.user_permissions.first().name)
        # group = Group.objects.first()
        # print(group)
        # print(group.permissions.first().name)
        # print(group.user_set.first().username)
        # permission = Permission.objects.filter(pk=2).first()
        # print(permission.name)
        # print(permission.user_set.first().username)
        # per = Permission.objects.filter(pk=2).first()
        # print(per.group_set.first().name)
        return APIResponse("OK")

class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return APIResponse("登录成功")

class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]
    # permission_classes = [MyPermission]
    def get(self, request, *args, **kwargs):
        return APIResponse("读成功")
    def post(self, request, *args, **kwargs):
        return APIResponse("写成功")

class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]
    def get(self, request, *args, **kwargs):
        return APIResponse("读成功")
    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")