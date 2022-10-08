import json

from django import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, reverse, get_object_or_404
from django.utils.decorators import method_decorator

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

    @method_decorator(
        user_passes_test(lambda user: user.has_perm('contacts.add_contact'))
    )
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().get(request, *args, **kwargs)

    @method_decorator(
        user_passes_test(lambda user: user.has_perm('contacts.add_contact'))
    )
    def post(self, request: HttpRequest) -> HttpResponse:
        contact_form = forms.ContactForm(request.POST)

        if contact_form.is_valid():
            models.Contact.objects.create(
                full_name=contact_form.cleaned_data['full_name'],
                phone_number=contact_form.cleaned_data['phone_number'],
                address=contact_form.cleaned_data['address'],
                owner=request.user,
            )
            return redirect(reverse('contacts:all'))
        return redirect(request.get_full_path())


class CreateContactsView(LoginRequiredMixin, views.View):
    def post(self, request: HttpRequest) -> HttpResponse:
        contacts_file = request.FILES['contacts']
        text_contacts = contacts_file.read().decode()
        raw_contacts = json.loads(text_contacts)

        for raw_contact in raw_contacts:
            models.Contact.objects.create(
                **raw_contact,
                owner=request.user
            )

        return redirect(reverse('contacts:all'))


class DeleteContactView(LoginRequiredMixin, views.View):
    @method_decorator(
        user_passes_test(lambda user: user.has_perm('contacts.delete_contact'))
    )
    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        contact = get_object_or_404(models.Contact, pk=pk)
        contact.delete()
        return redirect(reverse('contacts:all'))


class DownloadContactsView(LoginRequiredMixin, views.View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        contacts = models.Contact.objects.filter(owner=request.user)
        
        raw_contacts = [{
            'full_name': contact.full_name,
            'address': contact.address,
            'phone_number': contact.phone_number,
        } for contact in contacts]
        text_contacts = json.dumps(raw_contacts, indent=4)

        response = HttpResponse(text_contacts.encode(), content_type='text/json')
        response['Content-Disposition'] = (
            f'attachment; filename=contacts.json'
        )
        return response

