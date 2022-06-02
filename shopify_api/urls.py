from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    # path("login", views.login_user),
    path("access_scope",views.getAccessScopes),
    path("products", views.getAllProducts)

]