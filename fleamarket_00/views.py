from django.shortcuts import redirect, render, RequestContext, render_to_response
from django.contrib.auth import get_user_model
from shop.forms import UserCreationForm

User = get_user_model()

def register(request):

    if request.method == "GET":
        form = UserCreationForm()

        context = { 'form': form, }

        return render_to_response('register.html', RequestContext(request, context))

    elif request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

        else:
            print(form.errors)