import json
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rechan_shopping.forms import MemberForm
from rechan_shopping.models import Ads, Product


def index(request):
    return render(request, 'index.html', {
        'ads': Ads.objects.all().order_by('-publish_date'),
        'toys': Product.objects.filter(category='Toys').order_by('-id')[:3],
        'candies': Product.objects.filter(category='Candies').order_by('-id')[:3],
        'draws': Product.objects.filter(category='Lucky_draw').order_by('-id')[:3],
    })


def prod_list(request, cat):
    return render(request, 'prod_list.html', {
        'prods': Product.objects.filter(category=cat).order_by('-id')[:20]
    })

def product(request, prod_id):
    return render(request, 'product.html', {
        'prod': Product.objects.get(id=prod_id)
    })


def faq(request):
    return render(request, 'faq.html')

def profile(request):
    return render(request, 'profile.html')

def cart(request):
    return render(request, 'cart.html')

@csrf_exempt
def get_cart_items(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cartArray = []
        for i in data:
            item = Product.objects.get(id=i['id'])
            cartArray.append({
                "name": item.name,
                "Qtd": i['Qtd'],
                "price": item.price
                })
        return HttpResponse(
            json.dumps(cartArray),
            content_type='application.json'
        )



def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            form.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
    else:
        form = MemberForm()

    return render(request, "registration/register.html", {
        'form': form,
    })