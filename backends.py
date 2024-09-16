from django.contrib.auth.backends import ModelBackend

from school.models import CustomUser
from dreametrix.models import Admin

class PublicSchemaBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')
        try:
            user = Admin.objects.get(username=username)  # to check if email is better
            if user.check_password(password):
                return user
        except Admin.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Admin.objects.get(pk=user_id)
        except Admin.DoesNotExist:
            return None



class TenantSchemaBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        print("tenant schema backend")

        if username is None:
            username = kwargs.get('email')
        try:
            user = CustomUser.objects.get(username=username, password=password)
            if user:
                print("user exists")
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None