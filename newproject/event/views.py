from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewEventForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from .models import Event
from django.core.files.storage import FileSystemStorage


@login_required
def create_event(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect(event_list)
    else:
        form = NewEventForm()
    return render(request, 'create_event.html', {'form': form})



def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html',{
        'events':events
    })