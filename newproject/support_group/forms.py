from django import forms
from .models import SupportGroup

class NewSupportGroupForm(forms.ModelForm):
    # about = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #         ),
    # )

    class Meta:
        model = SupportGroup
        fields = ['title','goal','short_description', 'about','support_group_image']