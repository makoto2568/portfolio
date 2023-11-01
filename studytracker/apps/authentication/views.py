from .forms import SignupForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignupView(CreateView):
    template_name = 'authentication/signup.html'
    form_class = SignupForm
    success_url = '/authentication/user/'
    
    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return result


class LoginView(LoginView):
    template_name = 'authentication/login.html'
    form_class = LoginForm


class LogoutView(LogoutView):
    template_name = 'authentication/logout.html'


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/user.html'
    login_url = 'authentication/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class OtherView(LoginRequiredMixin, TemplateView):
    template_name = 'authentication/other.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.exclude(username=self.request.user.username)
        return context