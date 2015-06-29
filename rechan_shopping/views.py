import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rechan_shopping.forms import MemberForm
from rechan_shopping.models import Ads, Product
from django.core.paginator import Paginator


def index(request):
    return render(request, 'index.html', {
        'ads': Ads.objects.filter(activated=True).order_by('-publish_date'),
        'discounts': Product.objects.filter(discount_S=True).order_by('-id')[:8],
        'toys': Product.objects.filter(category='Toys').order_by('-id')[:8],
        'candies': Product.objects.filter(category='Candies').order_by('-id')[:8],
        'draws': Product.objects.filter(category='Lucky_draw').order_by('-id')[:8],
    })


# def prod_list(request, cat):
#     if cat == "Discount":
#         prods = Paginator(Product.objects.filter(discount_S=True).order_by('-id'), 4)
#     else:
#         prods = Paginator(Product.objects.filter(category=cat).order_by('-id'), 4)
#     return render(request, 'old_pages/prod_list.html', {
#         'prods': prods
#     })
#
# def product(request, prod_id):
#     return render(request, 'old_pages/product.html', {
#         'prod': Product.objects.get(id=prod_id)
#     })
#
# @user_passes_test(lambda u: u.is_superuser)
# def stock(request):
#     return render(request, 'old_pages/admin_manager/stock.html')
#
# @user_passes_test(lambda u: u.is_superuser)
# def stock_detail(request, prod_id):
#     return render(request, 'old_pages/admin_manager/stock_detail.html')
#
# @csrf_exempt
# def get_stock(request, cat):
#     stock = []
#     if request.method == 'GET':
#         if cat == "candies":
#             add = Product.objects.filter(category='Candies')
#         elif cat == "toys":
#             add = Product.objects.filter(category='Toys')
#         elif cat == "draws":
#             add = Product.objects.filter(category='Lucky_draw')
#         elif cat == "ads":
#             add = Ads.objects.filter(activated=True)
#         elif cat == "discounts":
#             add = Product.objects.filter(discount_S=True)
#         else:
#             add = ""
#         for obj in add:
#             stock.append({
#                 'id': obj.id,
#                 'name': obj.name,
#                 'have': obj.have,
#                 'discount': obj.discount_S
#             })
#     return HttpResponse(json.dumps(stock),
#                         content_type='application/json')
#
# def admin_purchase_confirm(request):
#     return render(request, 'old_pages/admin_manager/admin_purchase_confirm.html')
#
# def faq(request):
#     return render(request, 'old_pages/faq.html')
#
# def profile(request):
#     return render(request, 'old_pages/profile.html')
#
# def cart(request):
#     return render(request, 'old_pages/cart.html')
#
# @csrf_exempt
# def get_cart_items(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         cartArray = []
#         for i in data:
#             item = Product.objects.get(id=i['id'])
#             cartArray.append({
#                 "name": item.name,
#                 "Qtd": i['Qtd'],
#                 "price": item.price
#                 })
#         return HttpResponse(
#             json.dumps(cartArray),
#             content_type='application.json'
#         )
#
#
#
# def register(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST, request.FILES)
#         if form.is_valid():
#             username = request.POST["username"]
#             password = request.POST["password1"]
#             form.save()
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("index")
#     else:
#         form = MemberForm()
#
#     return render(request, "registration/register.html", {
#         'form': form,
#     })