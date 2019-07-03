from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewCampaignForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from .models import Campaign
from django.core.files.storage import FileSystemStorage
# Create your views here.


# def create_campaign(request):
#      campaign = get_object_or_404(Campaign, pk=pk)
#     user = User.objects.first()  # TODO: get the currently logged in user
#     if request.method == 'POST':
#         form = NewCampaignForm(request.POST)
#         if form.is_valid():
#             topic = form.save(commit=False)
#             topic.board = board
#             topic.starter = request.user
#             topic.save()
#             post = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 topic=topic,
#                 created_by=user
#             )
#             return redirect('campaign_list')  # TODO: redirect to the created topic page
#     else:
#         form = NewCampaignForm()
#     return render(request, 'create_campaign.html', {'form': form})

def create_campaign(request):
    if request.method == 'POST':
        form = NewCampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()
            return redirect(campaign_list)
    else:
        form = NewCampaignForm()
    return render(request, 'create_campaign.html', {'form': form})



def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html',{
        'campaigns':campaigns
    })