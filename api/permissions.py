from rest_framework.permissions import BasePermission
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from api.models import User
from api.throttle import SendMessageRate
from utils.response import APIResponse


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        username = request.data.get("username")
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            return True
        return False

class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [MyPermission]
    def get(self, request, *args, **kwargs):
        return APIResponse("读成功")
    def post(self, request, *args, **kwargs):
        return APIResponse("写成功")

class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]
    def get(self, request, *args, **kwargs):
        return APIResponse("读成功")
    def post(self, request, *args, **kwargs):
        return APIResponse("写成功")