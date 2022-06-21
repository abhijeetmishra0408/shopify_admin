from django.shortcuts import render
from .models import Campaign, CampaignReach, CampaignValue
import datetime
import random
import datetime
from datetime import date
from faker import Faker
from django.shortcuts import render
import requests
import os
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from decouple import config
from django.http import HttpResponse
import random
import string



@api_view(["GET"])
def insertCampaign(request):
    
    for i in range(30):
        try:
            ids = ''.join(random.choices(string.digits, k=8))
            price = ''.join(random.choices(string.digits, k=4))
            # print(type(ids), type(price), ids, price)
            campaign_details = Campaign(campaign_id = ids, spend = price)
            campaign_details.save()
            campaign_reach = CampaignReach(action_type = "link_click", value = ''.join(random.choices(string.digits, k=4)), oneday_view = ''.join(random.choices(string.digits, k=2)), oneday_click = ''.join(random.choices(string.digits, k=3)), cmpaign = campaign_details)
            campaign_reach.save()
            campaign_value = CampaignValue(action_type = "link_click", value = round(random.uniform(0.0, 0.9),10), oneday_view_cost = round(random.uniform(10.0, 30.9),10), oneday_click_cost = round(random.uniform(0.0, 0.9),10), cmpaign = campaign_details)
            campaign_value.save()


        except:
            raise
            pass

    return HttpResponse('campaign is created')

# Create your views here.
