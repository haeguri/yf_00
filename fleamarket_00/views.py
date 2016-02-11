from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from bs4 import BeautifulSoup

User = get_user_model()

# Create your views here.
def register(request):
    return render_to_response('register.html', request, {})