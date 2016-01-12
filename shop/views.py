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
        item_form = ItemForm

    context = {
        'item ': item_form
    }

    render_to_response('shop/item_new.html', context)
    # elif request.method == "POST":
    #     edit_form = PhotoEditForm(request.POST, request.FILES)
    #
    #     if edit_form.is_valid():
    #         new_photo = edit_form.save(commit=False)
    #         new_photo.user = request.user
    #         new_photo.save()
    #
    #         return redirect(new_photo.get_absolute_url())
    #
    # return render(
    #     request,
    #     'new_photo.html',
    #     {
    #         'form':edit_form,
    #     }
    # )