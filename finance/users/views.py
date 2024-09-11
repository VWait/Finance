from django.views.generic import FormView

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm



class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/logs')

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'btn_success_value': 'Войти'}


class Register(FormView):
    template_name = 'users/login.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return self.request.GET.get('next', '/logs')

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'btn_success_value': 'Зарегистрироваться'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
