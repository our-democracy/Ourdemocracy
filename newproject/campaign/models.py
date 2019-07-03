from django.db import models
from django.contrib.auth.models import User

# Create your models here.



CAMPAIGN_CATEGORY = (
    ('social cause','Social Cause'),
    ('journalism campaigns','Journalism Campaigns'),
    ('political campaigns','Political Campaigns'),
)
VERIFY_CAMPAIGN = (
    ('yes','Yes'),
    ('no','No')
)
STATUS_CAMPAIGN = (
    ('active','Active'),
    ('not active','Not Active'),
    ('deleted','Deleted'),
)

class Campaign(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CAMPAIGN_CATEGORY, default='social cause')
    goal = models.IntegerField()
    raised = models.IntegerField(null=True,default=0)
    day = models.IntegerField()
    short_description = models.CharField(max_length=255)
    about = models.TextField()
    campaign_image = models.ImageField(upload_to='campaigns/images/',null='True',blank='True')
    is_verified = models.CharField(max_length=20,choices=VERIFY_CAMPAIGN, default='no')
    status = models.CharField(max_length=30, choices =STATUS_CAMPAIGN, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='capmaigns')
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True, related_name='+')

    def __str__(self):
        return self.title