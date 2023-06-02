from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseForm, AccountForm

# Create your views here.

@login_required
def Receipt_List(request):
    receipt_list = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_list": receipt_list,
    }
    return render(request, "receipts/list.html", context)

@login_required
def Create_Receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create.html", context)

@login_required
def Category_List(request):
    category_list = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "category_list": category_list
    }
    return render(request, "categories/category_list.html", context)

@login_required
def Account_List(request):
    account_list = Account.objects.filter(owner=request.user)
    context = {
        "account_list": account_list
    }
    return render(request, "accounts/accounts_list.html", context)

@login_required
def Create_Category(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseForm()

    context = {
        "form": form,
    }

    return render(request, "categories/create_category.html", context)


@login_required
def Create_Account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/create_account.html", context)
