from django.forms import ModelForm

from .models import Category


class CategoryForm(ModelForm):
    increment = 0

    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs['id'] = f"{field_name}_{self.increment}"
            CategoryForm.increment += 1


class CategoryOnlyNameForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]