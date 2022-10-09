from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()
 
 
class Contact(models.Model):
    full_name = models.CharField(max_length=100, help_text='Full name')
    phone_number = models.CharField(max_length=20, help_text='Phone number')
    address = models.CharField(max_length=100, help_text='Address')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Creation date')
 
    owner = models.ForeignKey(
       UserModel,
       on_delete=models.CASCADE,
       related_name='contacts',
       help_text='Created by'
    )
 
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']

    def __str__(self) -> str:
        return (
            f'Contact of User ID={self.owner_id} for [{self.full_name}] '
            f'created at {self.created_at.date()}'
        )
 
