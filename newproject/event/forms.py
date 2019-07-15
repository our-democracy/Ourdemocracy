from django import forms
from .models import Event

class NewEventForm(forms.ModelForm):
    # about = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #         ),
    # )

    class Meta:
        model = Event
        fields = ['title','category','start_time','end_time','short_description', 'about','event_image']