from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import get_user_model
from .models import Item, Category
from .forms import ItemForm
from bs4 import BeautifulSoup

User = get_user_model()


# Create your views here.
def index(request):
    item_list = Item.objects.all()

    for item in item_list:
        soup = BeautifulSoup(item.desc, "html.parser")
        try:
            item.img_url = soup.find('img')['src']
        except:
            pass

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
        form = ItemForm(initial={'vendor':User.objects.get(email="admin@admin.com"),'category':Category.objects.get(name="판매")})

    elif request.method == "POST":
        form = ItemForm(data=request.POST)
        print(request.POST)
        print("실행이 됩니다.")

        if form.is_valid():
            new_item = form.save()
            # new_item.save()
            print("유효한 데이터입니다.")

            return redirect(new_item.get_absolute_url())

        else:
            print(form.errors)

    context = {
        'form': form,
        'vendor':User.objects.get(email="admin@admin.com"),
        'category':Category.objects.get(name="판매"),
    }

    return render(request, 'shop/item_new.html', context)
    # return render_to_response('shop/item_new.html', context)