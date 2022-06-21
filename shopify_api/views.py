from calendar import month
from email.mime import image
import imp
from itertools import count, product
from select import select
import stat
from django.shortcuts import render
import requests
import os
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view
from decouple import config
from django.http import HttpResponse
import os
from . models import Orders, Products, ProductsVariant
import datetime
from facebook_api.models import CampaignReach, CampaignValue, Campaign
# Create your views here.

# access_key = config("ACCESS_TOKEN")
access_key = os.environ.get("ACCESS_TOKEN")
@api_view(('GET',))
def getAccessScopes(request):
    print(config)
    url = "https://python-test-shop.myshopify.com/admin/oauth/access_scopes.json"
    payload = {
                
            }
    print(access_key)
    headers = {
        "X-Shopify-Access-Token":access_key,
        "content-type": "application/json"
        }
    print(headers)
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        print(" Status Success")
    elif r.status_code == 401:
        print(" Invalid or Unauthrized Access Key")
    elif r.status_code == 403:
        print("You dont have permission to access this data")
    # print("read_inventory" in r.json()['access_scopes'][0].values())
    # print(r.json()['access_scopes'])
    # for each in r.json()['access_scopes']:
    #     if "read_inventory" in each.values():
    #         print('--------------------')
    return HttpResponse('Hello! ' * times)


@api_view(["GET"])
def getAllProducts(request):
    url = "https://python-test-shop.myshopify.com/admin/api/2022-04/products.json"
    headers = {
        "X-Shopify-Access-Token":access_key,
        "content-type": "application/json"
        }
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        try:
            shopify_products_id = Products.objects.last().order_by("shopify_product_id")
        except:
            shopify_products_id = 0
        for product in r.json()["products"]:
            try:
                product_details = Products(shopify_product_id = product["id"], name = product["title"], body_html = product["body_html"], status = product["status"], handle = product["handle"], image = product["image"]["src"])
                product_details.save()
            except:
                product_details = Products.objects.filter(shopify_product_id = product["id"]).update(name = product["title"], body_html = product["body_html"], status = product["status"], handle = product["handle"], image = product["image"]["src"])

            for variants in product["variants"]:
                try:
                    product_variants = ProductsVariant(product_id = product_details.id, shopify_product_id = product["id"], shopify_Variant_id =variants["id"], price = variants["price"], sku = variants["sku"])
                    product_variants.save()
                except:
                    product_variants = ProductsVariant.objects.filter(shopify_Variant_id = variants["id"]).update(price = variants["price"], sku = variants["sku"])
            
        # with open('new_file.json', 'w') as f:
        #     json.dump(r.json(), f, indent=2)
        #     print("New json file is created from data.json file")
    elif r.status_code == 401:
        return HttpResponse('Invalid or Unauthrized Access Key')
    elif r.status_code == 403:
        return HttpResponse('You dont have permission to access this data')
    return HttpResponse('Product List is updated')
    # return render(request, 'index.html',{'message_name':"name"})
    # return Response({"data":r.json()}, status=HTTP_200_OK)

from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.forms.models import model_to_dict
from django.db.models.functions.datetime import ExtractMonth, ExtractYear
from django.db.models import Sum
from .serializers import BestProductSerializer
@api_view(["GET"])
def getHomePage(request):
    all_orders = Orders.objects.all()
    all_products = Products.objects.all()[0:10]
    chart_data = Orders.objects.annotate(month=TruncMonth('order_date'),yearmonth=ExtractMonth('order_date')).values('month', 'yearmonth').annotate(counts=Count('id')).values('yearmonth', 'counts').order_by("month")
    # print(chart_data)
    product_data = Orders.objects.values('product', 'product__name').annotate(total_price=Sum('price')).order_by("-total_price")[0:10]
    # print(BestProductSerializer(product_data, many = True).data)
    products = {"name":[], "total_price":[]}
    for each in product_data:
        products["name"].append(each["product__name"])
        products["total_price"].append(int(each["total_price"]))
    orders_data = {"labels":[], "data":[]}
    for each in chart_data:
        # print(each)
        orders_data["labels"].append(datetime.date(1900, each['yearmonth'], 1).strftime('%B'))
        orders_data["data"].append(each['counts'])
    orders = []
    for each in all_orders.filter()[0:10]:
        orders.append(
            {
                "id":each.id,
                "shopify_order_id":each.shopify_order_id,
                "price":each.price,
                "product":each.product.name
            }
        )
    facebook_campaign = {"id":[],"view":[], "click":[]}
    facebook_campaign_reach = CampaignReach.objects.all()[0:10]
    for each in facebook_campaign_reach:
        facebook_campaign["id"].append("ID: " + str(each.cmpaign.campaign_id))
        facebook_campaign["view"].append(str(each.oneday_view))
        facebook_campaign["click"].append(str(each.oneday_click))
    
    
    return render(request, 'index.html',{"chart_data":orders_data,"product_data":products,'orders':orders, "products":all_products, "orders_count":all_orders.count(), "sales":all_orders.aggregate(Sum('price')), "facebook_reach":facebook_campaign})

import random
import datetime
from datetime import date
from faker import Faker
@api_view(["GET"])
def insertOrders(request):
    product_variants = list(ProductsVariant.objects.all())
    range_choice = [5,6,8,10,12,15,17,19,20,3,5]
    fake = Faker()
    for i in range(200):
        random_product = random.choice(product_variants)
        print('-------------------')   
        print(random_product.id)
        # print(fake.date_time_between(start_date='-1y', end_date='now'))
        status_order = ["CONFIRMED", "PAID", "FAILED"]
        try:
            Orders.objects.create(shopify_order_id = random_product.shopify_Variant_id + i + random.choice(range_choice), currency = "INR", price = random_product.price, status = random.choice(status_order),product = random_product.product,productvariant = random_product,order_date = fake.date_time_between(start_date='-1y', end_date='now'))
        except:
            raise
    return HttpResponse('Product List is updated')