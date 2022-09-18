from django.urls import path

from . import views


urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
    path('add/', views.AddContactView.as_view(), name='add_contact'),
]

