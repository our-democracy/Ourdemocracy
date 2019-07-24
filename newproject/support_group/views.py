from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewSupportGroupForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from .models import SupportGroup
from django.core.files.storage import FileSystemStorage

@login_required
def create_support_group(request):
    if request.method == 'POST':
        form = NewSupportGroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            return redirect(support_group_list)
    else:
        form = NewSupportGroupForm()
    return render(request, 'create_support_group.html', {'form': form})



def support_group_list(request):
    groups = SupportGroup.objects.all()
    return render(request, 'support_group_list.html',{
        'groups':groups
    })