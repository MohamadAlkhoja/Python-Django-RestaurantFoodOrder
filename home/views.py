from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    mostordered = Product.objects.all()[:3]
    recentlyordered = Product.objects.all().order_by('-id')[:3]
    mainmeal = Product.objects.all().order_by('?')[:3]

    context = {'setting': setting, 'category': category, 'page': 'home', 'sliderdata': sliderdata,
               'mostordered': mostordered, 'recentlyordered': recentlyordered, 'mainmeal': mainmeal,}
    return render(request, 'index.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'aboutus'}
    return render(request, 'aboutus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'references'}
    return render(request, 'references.html', context)


def menu(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    productmenu = Product.objects.all()[:12]
    context = {'setting': setting, 'category': category, 'page': 'menu','productmenu': productmenu}
    return render(request, 'menu.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your Message Sent Successfully, Thank You")
            return HttpResponseRedirect ('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form}
    return render(request, 'contact.html', context)

def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {'products': products, 'category': category, 'categorydata': categorydata}
    return render(request, 'products.html', context)

def product_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    context = {'category': category,'product': product, 'images': images,}
    return render(request, 'product_detail.html', context)