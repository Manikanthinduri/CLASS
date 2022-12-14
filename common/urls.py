from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.registration, name='signup'),
    path('login/', views.login, name='login'),
    path('login/dashboard/', views.dashboard),
]