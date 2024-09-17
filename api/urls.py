from django.urls import path

from api import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/create", views.register_view, name="create"),
    path("/login", views.login_view, name="login"),
]