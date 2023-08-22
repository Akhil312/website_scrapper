from django.urls import path
from . import views

app_name="websitescraper_app"

urlpatterns = [
    path('',views.home,name="home"),

]