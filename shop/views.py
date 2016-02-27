from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.forms import inlineformset_factory

from .models import Item, Category, ItemPhoto
from .forms import ItemForm

from bs4 import BeautifulSoup

from time import strftime

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

        initial_data = {
            'category': Category.objects.get(name="판매"),
            'vendor': request.user,
            'name': strftime("%m-%d %H:%M:%S의 테스트 아이템"),
            'purchased_at': "최근",
            'shipping_price': "3000",
            'desc': "이것은 설명입니다.",
            'deal_place': "우리집",
            'deal_way': "direct",
            'condition': "S"
        }

        item_form = ItemForm(initial=initial_data)
        item = Item()
        item_photo_formset = ItemPhotoFormSet(instance=item)

    if request.method == "POST":
        item_form = ItemForm(data=request.POST)
        item = Item()
        item_photo_formset = ItemPhotoFormSet(instance=item)

        if item_form.is_valid():

            new_item = item_form.save(commit=False)
            new_item.vendor = request.user

            print(request.POST)
            print(request.FILES)

            item_photo_formset = ItemPhotoFormSet(request.POST, request.FILES, instance = new_item)

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
        'item_form': item_form,
        'item_photo_formset': item_photo_formset,
        'vendor': User.objects.get(email="admin@admin.com"),
        'category': Category.objects.get(name="판매"),
        'user': request.user
    }

    return render(request, 'shop/item_new.html', context)
    # return render_to_response('shop/item_new.html', context)