from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render(request, 'main/store.html', context)

def cart(request):
    context = {}
    return render(request, 'main/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'main/checkout.html', context)
