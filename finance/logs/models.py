from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    TYPES = {
        'revenue': 'Доход',
        'expense': 'Расход',
        'debt': 'Долг'
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=10, choices=TYPES.items())

    @staticmethod
    def get_group_category(user: User):
        categories = Category.objects.filter(user=user)

        grouped_categories = {category_type: [] for category_type in Category.TYPES.keys()}
        [grouped_categories[category.category_type].append(category) for category in categories]

        return grouped_categories

    def __str__(self):
        return self.name
