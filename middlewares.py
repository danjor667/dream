from django_tenants.middleware.main import TenantMainMiddleware
from django.conf import settings





class CustomMiddleware(TenantMainMiddleware):

    def process_request(self, request, **kwargs,):
        host = request.get_host().split(':')[0]

        if host in ('127.0.0.1', "localhost"):  # to be set to the domain
            request.auth_backend = "backends.PublicSchemaBackend"
            request.urlconf = "dreametrix.urls"
            settings.AUTHENTICATION_BACKENDS = [request.auth_backend]
        else:
            request.urlconf = "school.urls"
            settings.AUTH_USER_MODEL = "school.CustomUser"
            request.auth_backend = "backends.TenantSchemaBackend"
            settings.AUTHENTICATION_BACKENDS = [request.auth_backend]

        super().process_request(request)