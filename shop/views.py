from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list = Item.objects.all()

    context = {
        'item_list' : item_list,
    }

    return render_to_response('shop/index.html', context)

def item_detail(request, item_id):

    item = Item.objects.get(pk=item_id)

    context = {
        'item' : item
    }

    return render_to_response('shop/item_detail.html', context)

def item_new(request):

    if request.method == "GET":
        form = ItemForm()

    elif request.method == "POST":
        form = ItemForm(request.POST)

        if form.is_valid():
            new_item = form.save()
            # new_item.save()

            return render_to_response(new_item.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, 'shop/item_new.html', context)
    # return render_to_response('shop/item_new.html', context)