from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Hello.as_view()),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('logs/', include('logs.urls'))
]
