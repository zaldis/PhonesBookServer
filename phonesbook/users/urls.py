from django.urls import path

from . import views


urlpatterns = [
    path('new-user', views.CreateNewUserView.as_view(), name='new-user'),
]

