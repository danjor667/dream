from django.contrib import admin
from dreametrix import views

from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.public_index, name="index_public"),
    path('api', include('api.urls')),
]