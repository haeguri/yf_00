from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Item

# Create your views here.
def index(request):
    item_list = Item.objects.all()

    context = {
        'item_list' : item_list,
    }

    return render_to_response('shop/index.html', context)