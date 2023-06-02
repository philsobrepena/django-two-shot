from django.urls import path
from receipts.views import Receipt_List, Create_Receipt, Category_List, Account_List, Create_Category, Create_Account

urlpatterns = [
    path("accounts/create/", Create_Account, name="create_account"),
    path("categories/create/", Create_Category, name="create_category"),
    path("accounts/", Account_List, name="account_list"),
    path("categories/", Category_List, name="category_list"),
    path("create/", Create_Receipt, name="create_receipt"),
    path("", Receipt_List, name="home"),
]
