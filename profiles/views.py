from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from bs4 import BeautifulSoup

User = get_user_model()

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    items_of_user = user.item_set.order_by('-created_at')

    for item in items_of_user:
        soup = BeautifulSoup(item.desc, "html.parser")
        try:
            item.img_url = soup.find('img')['src']
        except:
            pass
    context = {
        'user':request.user,
        'items_of_user':items_of_user,
    }

    return render(request, 'profile.html', context)
