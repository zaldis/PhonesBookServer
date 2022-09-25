from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from contacts.models import Contact
from .models import User


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0
 
 
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = [ContactInline, ]

