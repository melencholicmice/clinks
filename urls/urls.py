from django.urls import path
from . import views

urlpatterns = [
    path('<str:short_url>/', views.redirect_to_full_url, name='redirect_to_full_url'),
]