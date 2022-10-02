from django import views
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, reverse, get_object_or_404

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

        query = request.GET.get('q', '')
        if query:
            contacts = contacts.filter(
                full_name__icontains=query
            )

        context['contacts'] = contacts
        context['query'] = query
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


class DeleteContactView(LoginRequiredMixin, views.View):
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        contact = get_object_or_404(models.Contact, pk=pk)
        contact.delete()
        return redirect(reverse('contacts'))

