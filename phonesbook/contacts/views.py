# from django.shortcuts import render
# from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView


# def contacts(request):
#     html = b"<h1>Hello, world!</h1>"
#     return HttpResponse(html)


# def contacts(request: HttpRequest) -> HttpResponse:
#     return render(request, 'contacts/my-contacts.html', {})
# 
# 
# def add_contact(request: HttpRequest) -> HttpResponse:
#     return render(request, 'contacts/add-contact.html', {})


class ContactsView(TemplateView):
    template_name = 'contacts/my-contacts.html'


class AddContactView(TemplateView):
    template_name = 'contacts/add-contact.html'

