from django.shortcuts import render
import requests
from shop.models import product
# Create your views here.
def home(request):
    return render(request, 'shop/home.html')


def load_product(request):
 p=requests.get('https://fakestoreapi.com/products')
 online_data=p.json()
 print(online_data)
 for i in online_data:
    insert_product=product(
        title=i['title'],
        price=i['price'],
        description=i['description'],
        image_url=i['image']
        

    )
    insert_product.save()
 return render(request, 'shop/home.html')


def shop(request):
    products=product.objects.all()
    context={'all_products':products}
    return render(request, 'shop/store.html',context)


def detail_product(request, product_id):
    theProduct=product.objects.get(pk=product_id)
    last_product=None
    if 'last_product_checked' in request.session:
        if product_id in request.session['last_product_checked']:
            request.session['last_product_checked'].remove(product_id)
        
        request.session['last_product_checked'].insert(0,product_id)
        last_product=product.objects.filter(pk__in=request.session['last_product_checked'])

        if len(request.session['last_product_checked'])>5:
            request.session['last_product_checked'].pop()

    else:
        request.session['last_product_checked']=[product_id]
    request.session.modified=True
    context={'product':theProduct,'last_checked':last_product}
    return render(request, 'shop/product.html',context)