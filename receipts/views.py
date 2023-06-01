from django.shortcuts import render, redirect
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm

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
