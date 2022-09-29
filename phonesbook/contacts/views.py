from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ContactsView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts/my-contacts.html'


class AddContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts/add-contact.html'

