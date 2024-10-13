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

    # Page for new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]