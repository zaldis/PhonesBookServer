from django.urls import path

from . import views


urlpatterns = [
    path('', views.GetContactsView.as_view(), name='contacts'),
    path('add/', views.CreateContactView.as_view(), name='add_contact'),
    path('<int:pk>/delete/', views.DeleteContactView.as_view(), name='delete_contact')
]

