from django.urls import path

from . import views


urlpatterns = [
    path("categories/", views.Categories.as_view(), name='categories'),
    path("category/<str:category_type>/create", views.CategoryCreateView.as_view(), name='category-create'),
    path("category/<slug:pk>/update", views.CategoryUpdateView.as_view(), name='category-update'),
    path("category/<slug:pk>/delete", views.CategoryDeleteView.as_view(), name='category-delete'),
    path("accounts/", views.Accounts.as_view(), name='accounts'),
    path("notes/", views.Notes.as_view(), name='notes'),
]
