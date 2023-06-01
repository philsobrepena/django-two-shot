from django.urls import path
from receipts.views import Receipt_List, Create_Receipt

urlpatterns = [
    path("create/", Create_Receipt, name="create_receipt"),
    path("", Receipt_List, name="home"),
]
