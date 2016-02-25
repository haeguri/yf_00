from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.forms import inlineformset_factory

from .models import Item, Category, ItemPhoto
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

    ItemPhotoFormSet = inlineformset_factory(Item, ItemPhoto, fields=('image',), can_delete=False, extra=2)

    if request.method == "GET":

        item = Item()
        item_photo_formset = ItemPhotoFormSet(instance=item)

        item_form = ItemForm(initial={'category':Category.objects.get(name="판매")})

    elif request.method == "POST":
        item_form = ItemForm(data=request.POST)

        if item_form.is_valid():

            new_item = item_form.save(commit=False)
            new_item.vendor = request.user

            item_photo_formset = ItemPhotoFormSet(request.POST, instance = new_item)

            if item_photo_formset.is_valid():
                new_item.save()
                item_photo_formset.save()

                return redirect(new_item.get_absolute_url())

            else:
                print(item_photo_formset.errors)

            # new_item.vendor = request.user
            # new_item.save()

        else:
            print("item_form is_valid is not true")
            print(item_form.errors)

    context = {
        'item_form':item_form,
        'item_photo_formset':item_photo_formset,
        'vendor':User.objects.get(email="admin@admin.com"),
        'category':Category.objects.get(name="판매"),
        'user': request.user
    }

    return render(request, 'shop/item_new.html', context)
    # return render_to_response('shop/item_new.html', context)