from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Item, Category
from .forms import ItemForm
from bs4 import BeautifulSoup

User = get_user_model()


# Create your views here.
def index(request):
    item_list = Item.objects.order_by('-created_at')[:50]

    for item in item_list:
        soup = BeautifulSoup(item.desc, "html.parser")
        try:
            item.img_url = soup.find('img')['src']
        except:
            pass

    context = {
        'item_list' : item_list,
        'user': request.user,
    }

    return render_to_response('shop/index.html', context)

def item_detail(request, item_id):

    item = Item.objects.get(pk=item_id)

    context = {
        'item' : item,
        'user': request.user,
    }

    return render_to_response('shop/item_detail.html', context)

@login_required
def item_new(request):

    if request.method == "GET":
        form = ItemForm(initial={'category':Category.objects.get(name="판매"), 'vendor':request.user})

    elif request.method == "POST":
        form = ItemForm(data=request.POST)

        if form.is_valid():
            new_item = form.save()
            # new_item.vendor = request.user
            # new_item.save()

            return redirect(new_item.get_absolute_url())

        else:
            print(form.errors)

    context = {
        'form': form,
        'vendor':User.objects.get(email="admin@admin.com"),
        'category':Category.objects.get(name="판매"),
        'user': request.user
    }

    return render(request, 'shop/item_new.html', context)
    # return render_to_response('shop/item_new.html', context)