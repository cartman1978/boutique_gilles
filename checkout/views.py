from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {}) 
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HTibYKKfQej5WyLgCJK7monNBPCYZjPlh1Ct2DMnbewd12uqOEpbaBjgHOjr7ozzYJcVdNfhYcxEh47lCCE0Pho0022hS3ROM',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)