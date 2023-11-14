from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterUserForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from vpn.models import ProxyURLObj


class UserCreate(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class UserAuth(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/auth.html'
    
    def get_success_url(self):
        return '/'


def user_account(request):
    return render(request, 'users/user_area.html')



def logout_user(request):
    logout(request)
    return redirect('home')