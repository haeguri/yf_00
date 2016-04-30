from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.forms import inlineformset_factory
from django.http import HttpResponse

from .models import Item, Category, ItemPhoto, ItemComment
from .forms import ItemForm
from django.template import loader

from time import strftime

import json

User = get_user_model()


# Create your views here.
def index(request):
    item_list = Item.objects.order_by('-created_at')[:50]

    context = {
        'item_list' : item_list,
        'user': request.user,
    }

    return render_to_response('shop/index.html', context)

def item_detail(request, item_id):

    item = Item.objects.get(pk=item_id)

    context = {
        'item' : item,
        'user': request.user
    }

    return render(request, 'shop/item_detail.html', context)


@login_required()
def item_edit(request, item_id):

    before_item = Item.objects.get(id=item_id)
    is_vendor = (request.user == before_item.vendor)

    if is_vendor:
        ItemPhotoFormSet = inlineformset_factory(Item, ItemPhoto, fields=('image',), can_delete=False, extra=8)

        if request.method == "GET":

            initial_data = {
                'category': before_item.category,
                'state':before_item.state,
                'photos_of_item': before_item.photos_of_item,
                'vendor': before_item.vendor,
                'name': before_item.name,
                'include_shipping': before_item.include_shipping,
                'price': before_item.price,
                'desc': before_item.desc,
                'deal_place': before_item.deal_place,
                'deal_way': before_item.deal_way,
                'condition': before_item.condition
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

                item_photo_formset = ItemPhotoFormSet(request.POST, request.FILES, instance = new_item)

                if item_photo_formset.is_valid():
                    new_item.save()
                    item_photo_formset.save()

                    return redirect(new_item.get_absolute_url())

                else:
                    print(item_photo_formset.errors)

            else:
                print("item_form is_valid is not true")
                print(item_form.errors)

        context = {
            'item_form': item_form,
            'item_photo_formset': item_photo_formset,
            'user': request.user,
            'title': '물품수정'
        }

    else:
        return redirect('shop:item_detail', item_id)

    return render(request, 'shop/item_form.html', context)

@login_required()
def comment(request):
    response_data = {}

    if request.method == 'POST':

        if request.POST.get('body') == None:
            comment_id = request.POST.get('comment')
            i_comment = ItemComment.objects.get(id=comment_id)
            i_comment.delete()

            response_data['status'] = "this isn't happening"

        else:

            body = request.POST.get('body')
            item_id = request.POST.get('item')
            user_id = request.POST.get('user')
            item = Item.objects.get(id=item_id)
            user = User.objects.get(id=user_id)

            comment = ItemComment(body=body, item=item, user=user)
            comment.save()

            template = loader.get_template('shop/comment.html')

            response_data['comment'] = template.render({
                'item_comment':ItemComment.objects.filter(id=comment.id),
                'user':request.user
            })

    else:
        response_data['nothing to see'] = "this isn't happening"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required
def item_new(request):

    ItemPhotoFormSet = inlineformset_factory(Item, ItemPhoto, fields=('image',), can_delete=False, extra=8)

    if request.method == "GET":

        initial_data = {
            'category': Category.objects.get(name="판매"),
            'state':'sale',
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

            item_photo_formset = ItemPhotoFormSet(request.POST, request.FILES, instance = new_item)

            if item_photo_formset.is_valid():
                new_item.save()
                item_photo_formset.save()

                return redirect(new_item.get_absolute_url())

            else:
                print(item_photo_formset.errors)

        else:
            print("item_form is_valid is not true")
            print(item_form.errors)

    context = {
        'item_form': item_form,
        'item_photo_formset': item_photo_formset,
        'user': request.user,
        'title': '물품등록'
    }

    return render(request, 'shop/item_form.html', context)