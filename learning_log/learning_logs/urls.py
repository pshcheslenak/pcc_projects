"""Defines URL pattern for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # List of topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    # Page for a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for an entry editing
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]