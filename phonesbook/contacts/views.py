from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, reverse

from . import forms, models


class GetContactsView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts/my-contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        contacts = (
            models.Contact.objects.filter(owner=request.user)
                .defer('owner', 'created_at')
        )
        context['contacts'] = contacts
        return context 


class CreateContactView(LoginRequiredMixin, TemplateView):
    template_name = 'contacts/add-contact.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            models.Contact.objects.create(
                full_name=contact_form.cleaned_data['full_name'],
                phone_number=contact_form.cleaned_data['phone_number'],
                address=contact_form.cleaned_data['address'],
                owner=request.user,
            )
            return redirect(reverse('contacts'))
        return redirect(request.get_full_path())

