from rest_framework.serializers import ModelSerializer

from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone_number', 'address']

