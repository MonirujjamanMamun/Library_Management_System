from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages


class UserRegistrationView(FormView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form)  # form_valid function call hobe jodi sob thik thake


# class UserLoginView(LoginView):
#     template_name = 'login.html'

#     def get_success_url(self):
#         return reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')


def user_logout(request):
    messages.success(request, 'Log Out Successful.')
    logout(request)
    return redirect('login')
