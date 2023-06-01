from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.

def Receipt_List(request):
    receipt_list = Receipt.objects.all()
    context = {
        "receipt_list": receipt_list,
    }
    return render(request, "receipts/list.html", context)
