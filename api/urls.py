from os import path

from api import views

urlpatterns = [
    path('', views.index, name='index'),
]