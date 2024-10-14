"""Defines URL pattern for users."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include URL authority by default
    path('', include('django.contrib.auth.urls')),
]