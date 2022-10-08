from django.urls import path

from . import views


app_name = 'contacts'


urlpatterns = [
    path('', views.GetContactsView.as_view(), name='all'),
    path('add/', views.CreateContactView.as_view(), name='add'),
    path('add-from-file/', views.CreateContactsView.as_view(), name='add_from_file'),
    path('download/', views.DownloadContactsView.as_view(), name='download'),
    path('<int:pk>/delete/', views.DeleteContactView.as_view(), name='delete')
]

