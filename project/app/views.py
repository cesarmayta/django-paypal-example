from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

def view_return(request):
    return render(request,'return.html')

def view_cancel(request):
    return render(request,'cancel.html')

def view_that_asks_for_money(request):

    # What you want the button to do.
    host = request.get_host()
    paypal_dict = {
        "business":"sb-behd324044726@business.example.com",
        "amount": "100.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        'notify_url':'http://' + host + '/' + 'paypal',
        'return_url':'http://' + host + '/' + 'returnpage'
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)

