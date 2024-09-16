from django.urls import path, include

from school import views
from school.admin import tenant_admin

urlpatterns = [
    path("admin/", tenant_admin.urls),
    path('', views.index_tenant, name='index'),
    path('api', include('api.urls')),
]