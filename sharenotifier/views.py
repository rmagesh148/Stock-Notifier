from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from sharenotifier.forms import AddForm
from sharenotifier.models import StockDetails as sd

# Create your views here.


def index(request):
    google_login_page = 'http://127.0.0.1:8000/accounts/google/login'
    facebook_login_page = 'http://127.0.0.1:8000/accounts/facebook/login'
    return render(request, 'index.html', {'google_login_page': google_login_page, 'facebook_login_page': facebook_login_page})


def homepage(request):
    if request.method == 'GET':
        add_form = AddForm()
        user = User.objects.get(username=request.user)
        print user.id,"udwe id"
        extract_data = SocialAccount.objects.get(user_id=user.id)
        email = extract_data.extra_data['email']
        first_name = user.first_name
        stock_values = sd.objects.all()
        if stock_values:
            return render(request,'homepage.html', {'first_name':first_name, 'form': add_form, 'stock_values':stock_values})
        else:
            return render(request, 'homepage.html',
                          {'first_name': first_name, 'form': add_form, "message": "OOPS! You've no items to show up."})
    return render(request, 'homepage.html')


# def logout(request):
#     if request.method == 'GET':
#         user = User.objects.get(username=request.user)
#         user_delete = SocialAccount.objects.get(user_id=user.id)
#         user_delete.delete()
#         return HttpResponseRedirect('/')