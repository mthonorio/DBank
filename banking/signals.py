from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from rest_framework.authtoken.models import Token

@receiver(user_logged_in)
def create_auth_token(sender, user, request, **kwargs):
    Token.objects.get_or_create(user=user)
    print("Token created for user:", user.username, Token.objects.get(user=user).key)
