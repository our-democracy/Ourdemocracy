from django.db import models
from django.contrib.auth.models import User

# Create your models here.



EVENT_CATEGORY = (
    ('social event','Social Event'),
    ('journalism event','Journalism Event'),
    ('political event','Political Event'),
)
VERIFY_EVENT = (
    ('yes','Yes'),
    ('no','No')
)
STATUS_EVENT = (
    ('active','Active'),
    ('not active','Not Active'),
    ('deleted','Deleted'),
)

class Event(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=EVENT_CATEGORY, default='social event')
    location = models.CharField(max_length=255,null=True, blank=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    short_description = models.CharField(max_length=255)
    about = models.TextField()
    event_image = models.ImageField(upload_to='EventsImg',null='True',blank='True')
    is_verified = models.CharField(max_length=20,choices=VERIFY_EVENT, default='no')
    status = models.CharField(max_length=30, choices =STATUS_EVENT, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='events')
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.title