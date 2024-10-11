from django.shortcuts import render
from .models import Topic

def index(request):
    """Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topic."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
