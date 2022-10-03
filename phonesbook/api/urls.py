from django.urls import path
from rest_framework.authtoken import views as drf_views

from . import views


urlpatterns = [
    path('contacts/', views.GetContactsAPIView.as_view(), name='contacts'),
    path('token/', drf_views.obtain_auth_token),
]

