from django.urls import path

from . import views

urlpatterns = [
    path("accounts/", views.Accounts.as_view(), name='accounts'),
    path("categories/", views.Categories.as_view(), name='categories'),
    path("notes/", views.Notes.as_view(), name='notes')
]
