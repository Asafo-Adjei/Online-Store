from django.shortcuts import render,redirect
from item.models import Category, Item   #"item.models" --> where "item" is the name of the app folder the models.py file exists

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()

    return render(request, "storeapp/index.html", {
        'categories': categories,
        'items': items, 
    })

def contact(request):
    return render(request, 'storeapp/contact.html')

def signup(request):
    if request.method == 'post':
        form = SignupForm(request.post)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'storeapp/signup.html', {
        'form': form 
    })