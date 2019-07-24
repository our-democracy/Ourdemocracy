from django.db import models
from django.contrib.auth.models import User

# Create your models here.

VERIFY_GROUP = (
    ('yes','Yes'),
    ('no','No')
)
STATUS_GROUP = (
    ('active','Active'),
    ('not active','Not Active'),
    ('deleted','Deleted'),
)

class SupportGroup(models.Model):
    title = models.CharField(max_length=100, unique=True)
    goal = models.IntegerField()
    short_description = models.CharField(max_length=255)
    about = models.TextField()
    support_group_image = models.ImageField(upload_to='SupportGroup')
    is_verified = models.CharField(max_length=20,choices=VERIFY_GROUP, default='no')
    status = models.CharField(max_length=30, choices =STATUS_GROUP, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='supportgroup')
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.title