from django.shortcuts import render
from sharenotifier.forms import LoginForm
from allauth.socialaccount import providers
from django.conf import settings
# Create your views here.

def index(request):
    #form = LoginForm()
    google_login_page = 'http://127.0.0.1:8000/accounts/google/login'
    facebook_login_page = 'http://127.0.0.1:8000/accounts/facebook/login'
    return render(request, 'index.html', {'google_login_page': google_login_page, 'facebook_login_page': facebook_login_page})


def homepage(request):
    #email = providers('email','')
    print type(providers)
    return render(request,'homepage.html')
