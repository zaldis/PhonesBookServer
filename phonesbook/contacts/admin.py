from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'address', 'created_at', )
    fields = ('full_name', 'phone_number', 'address', 'owner', 'created_at', )
    readonly_fields = ('owner', 'created_at', )
    list_filter = ('owner', )
    search_fields = ('full_name', )

