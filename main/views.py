from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.

# @cache_page(60 * 5)
def index(request):
    return render(request, 'main/index.html')

@cache_page(60 * 5)
def about(request):
    return render(request, 'main/about.html')

@cache_page(60 * 5)
def services(request):
    return render(request, 'main/services.html')

# @cache_page(60 * 5)
def contact(request):
    return render(request, 'main/contact.html')

