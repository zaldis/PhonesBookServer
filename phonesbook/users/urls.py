from django.urls import path

from . import views


urlpatterns = [
    path('new-user', views.CreateUserView.as_view(), name='new-user'),
]

