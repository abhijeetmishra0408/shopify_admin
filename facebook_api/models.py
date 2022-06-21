# from pyexpat import model
# from turtle import mode
from django.db import models

# Create your models here.


class Campaign(models.Model):
    campaign_id = models.DecimalField(max_digits=16, decimal_places=0)
    spend = models.DecimalField(max_digits=7, decimal_places=2)


class CampaignReach(models.Model):
    cmpaign = models.ForeignKey("Campaign", on_delete=models.CASCADE, null=True)
    action_type = models.CharField(max_length=30, null=True)
    value = models.DecimalField(max_digits=8, decimal_places=0)
    oneday_view = models.DecimalField(max_digits=8, decimal_places=0)
    oneday_click = models.DecimalField(max_digits=8, decimal_places=0)

class CampaignValue(models.Model):
    cmpaign = models.ForeignKey("Campaign", on_delete=models.CASCADE, null=True)
    action_type = models.CharField(max_length=30, null=True)
    value = models.DecimalField(max_digits=16, decimal_places=12)
    oneday_view_cost = models.DecimalField(max_digits=16, decimal_places=12)
    oneday_click_cost = models.DecimalField(max_digits=16, decimal_places=12)
