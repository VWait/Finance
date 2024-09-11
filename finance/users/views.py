from django.views.generic import FormView

from django.contrib.auth.forms import UserCreationForm



class Login(FormView):
    template_name = 'users/login.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return self.request.GET.get('next', '/logs')
