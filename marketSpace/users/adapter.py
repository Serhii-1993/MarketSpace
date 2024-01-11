from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = f'/api/user/{request.user.id}'
        return path

    def get_signup_redirect_url(self, request):
        path = f'/api/user/{request.user.id}'
        return path
