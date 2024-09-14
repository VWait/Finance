from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Category


@method_decorator(login_required, name='get')
class Accounts(TemplateView):
    template_name = 'logs/accounts.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'path_name': 'accounts'}


@method_decorator(login_required, name='get')
class Categories(TemplateView):
    template_name = 'logs/categories.html'

    def get_context_data(self, **kwargs):
        context = {
            'path_name': 'categories',
            'content': Category.get_grouped_categories(self.request.user)
        }
        return super().get_context_data() | context


@method_decorator(login_required, name='get')
class Notes(TemplateView):
    template_name = 'logs/notes.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'path_name': 'notes'}
