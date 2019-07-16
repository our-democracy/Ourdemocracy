from django import forms
from .models import Event
# from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class NewEventForm(forms.ModelForm):
    # about = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #         ),
    # )

    # date_field = forms.DateField(widget=DatePicker())
    # date_field_required_with_min_max_date = forms.DateField(
    #     required=True,
    #     widget=DatePicker(
    #         options={
    #             'minDate': '2009-01-20',
    #             'maxDate': '2017-01-20',
    #         },
    #     ),
    # )
    # time_field = forms.TimeField(
    #     """
    #     In this example, the date portion of `defaultDate` is irrelevant;
    #     only the time portion is used. The reason for this is that it has
    #     to be passed in a valid MomentJS format. This will default the time
    #     to be 14:56:00 (or 2:56pm).
    #     """
    #     widget=TimePicker(
    #         options={
    #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
    #             'defaultDate': '1970-01-01T14:56:00'
    #         },
    #         attrs={
    #             'input_toggle': True,
    #             'input_group': False,
    #         },
    #     ),
    # )
    # start_time = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    # )

    # end_time = forms.DateTimeField(
    #     widget=DateTimePicker(
    #         options={
    #             'useCurrent': True,
    #             'collapse': False,
    #         },
    #         attrs={
    #             'append': 'fa fa-calendar',
    #             'icon_toggle': True,
    #         }
    #     ),
    # )

    start_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    end_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Event
        fields = ['title','category','start_time','end_time','short_description', 'about','event_image']