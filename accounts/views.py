import django.views.generic
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


# class ResetPasswordView(UpdateView):
#     form_class = PasswordResetForm
#     success_url = reverse_lazy('reset_password')
#     template_name = 'accounts/reset_password.html'
