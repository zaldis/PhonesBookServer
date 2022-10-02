from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View

from .forms import RegistrationForm


UserModel = get_user_model()


class CreateUserView(View):
    
    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request, 'users/new_user.html', {})

    def post(self, request, *args, **kwargs) -> HttpResponse:
        # Validate input
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            username = registration_form.cleaned_data['username']
            email = registration_form.cleaned_data['email']
            password = registration_form.cleaned_data['password']

            # Create and authenticate new users
            new_user = UserModel.objects.create_user(username=username, email=email, password=password)
            login(request, new_user)

            # Redirect to the page with contacts
            my_contacts_url = reverse('contacts')
            return redirect(my_contacts_url)

        return render(request, 'users/new_user.html', {'errors': registration_form.errors})

