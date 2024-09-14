from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from .models import Category
from .forms import CategoryForm, CategoryOnlyNameForm


@method_decorator(login_required, name='post')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('categories')

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user'] = request.user
        request.POST['category_type'] = self.kwargs['category_type']
        return super().post(request, *args, **kwargs)


@method_decorator(login_required, name='post')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryOnlyNameForm
    success_url = reverse_lazy('categories')


@method_decorator(login_required, name='post')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories')


@method_decorator(login_required, name='get')
class Categories(TemplateView):
    template_name = 'logs/categories.html'

    def get_context_data(self, **kwargs):
        context = {
            'path_name': 'categories',
            'content': self.get_content()
        }
        return super().get_context_data() | context

    def get_content(self):
        content = Category.get_grouped_categories(self.request.user)

        for category_type in content:
            for category in category_type['categories']:
                category.form = CategoryOnlyNameForm(initial={'name': category.name})
            category_type['form'] = CategoryOnlyNameForm()

        return content


@method_decorator(login_required, name='get')
class Accounts(TemplateView):
    template_name = 'logs/accounts.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'path_name': 'accounts'}


@method_decorator(login_required, name='get')
class Notes(TemplateView):
    template_name = 'logs/notes.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data() | {'path_name': 'notes'}
