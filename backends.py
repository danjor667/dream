from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


User = get_user_model()

class PublicSchemaBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')
        try:
            print("1111")
            user = User.objects.get(email=username)  # to check if email is better
            print("trying the user")
            if user.check_password(password):
                print("returning the user")
                return user
        except User.DoesNotExist:
            print("user does not exist")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None



# class TenantSchemaBackend(ModelBackend):
#
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         print("tenant schema backend")
#
#         if username is None:
#             username = kwargs.get('email')
#         try:
#             user = CustomUser.objects.get(username=username, password=password)
#             if user:
#                 print("user exists")
#                 return user
#         except CustomUser.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None