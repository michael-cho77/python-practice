from django.urls import path
from .views import *


app_name = "asyncapp"
urlpatterns = [
    path("", homeview, name="home"),
    path("articlecreate/", articlecreateview, name="articlecreate"),
]
