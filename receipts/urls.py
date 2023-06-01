from django.urls import path
from receipts.views import Receipt_List

urlpatterns = [
    path("", Receipt_List, name="home"),
]
