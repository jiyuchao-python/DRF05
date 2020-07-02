from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from api.models import User

class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', None)
        print(auth)
        if auth is None:
            return None
        auth_list = auth.split()
        if not (len(auth_list) == 2 and auth_list[0].lower() == "auth"):
            raise exceptions.AuthenticationFailed("认证失败")
        if auth_list[1] != "aaa.bbb.111":
            raise exceptions.AuthenticationFailed("信息错误，认证失败")
        user = User.objects.filter(username="admin123").first()
        if not user:
            raise exceptions.AuthenticationFailed("用户名不存在")
        print(user)
        return (user, None)
