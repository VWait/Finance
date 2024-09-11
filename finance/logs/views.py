from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='get')
class Logs(TemplateView):
    template_name = 'logs/logs.html'
