from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from sharenotifier.forms import AddForm
from sharenotifier.models import StockDetails as sd
from django import forms

# Create your views here.


def index(request):
    google_login_page = 'http://127.0.0.1:8000/accounts/google/login'
    facebook_login_page = 'http://127.0.0.1:8000/accounts/facebook/login'
    return render(request, 'index.html', {'google_login_page': google_login_page, 'facebook_login_page': facebook_login_page})


def homepage(request):
    if request.method == 'GET':
        add_form = AddForm()
        extract_data = SocialAccount.objects.get(user_id=request.user.id)
        img_src = extract_data.extra_data['picture']
        first_name = request.user.first_name
        stock_values = sd.objects.all()
        return render(request,'homepage.html',
                      {'first_name':first_name, 'form': add_form, 'stock_values':stock_values,
                       'img_src': img_src, "message": "OOPS! You've no items to show up."})

    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            company_code = form.cleaned_data['company_code']
            target_price = form.cleaned_data['target_price']
            extract_data = SocialAccount.objects.get(user_id=request.user.id)
            img_src = extract_data.extra_data['picture']
            first_name = request.user.first_name
            stock_values = sd.objects.all()
            if sd.objects.filter(company_code = company_code,user_id = request.user.id).exists():
                return render(request, 'homepage.html',
                              {'first_name': first_name,'form':form, 'stock_values': stock_values,
                               'img_src': img_src, 'info_message_red': 'Same Company code!',
                               "message": "OOPS! You've no items to show up."})

            form = AddForm()
            sd.objects.create(company_code=company_code,target_price=target_price,user_id=request.user.id)
            return render(request, 'homepage.html',
                          {'first_name': first_name, 'form': form, 'stock_values': stock_values,
                           'img_src': img_src, 'info_message_green': 'Company code and Price added!',
                           "message": "OOPS! You've no items to show up."})

def delete(request):
    if request.method == "GET":
        add_form = AddForm()
        extract_data = SocialAccount.objects.get(user_id=request.user.id)
        img_src = extract_data.extra_data['picture']
        first_name = request.user.first_name
        stock_values = sd.objects.all()
        delete_stock = sd.objects.filter(company_code=request.GET.get('delete',''),user_id=request.user.id)
        if delete_stock:
            delete_stock.delete()
            return render(request, 'homepage.html',
                          {'first_name': first_name, 'form': add_form, 'stock_values': stock_values,
                           'img_src': img_src, "message": "OOPS! You've no items to show up.",
                           'delete_message':'Deleted!!'})
        return render(request, 'homepage.html',
                          {'first_name': first_name, 'form': add_form, 'stock_values': stock_values,
                           'img_src': img_src, "message": "OOPS! You've no items to show up.",
                           'delete_message': 'Not Deleted, may be some issue!!'})




# def logout(request):
#     if request.method == 'GET':
#         user = User.objects.get(username=request.user)
#         user_delete = SocialAccount.objects.get(user_id=user.id)
#         user_delete.delete()
#         return HttpResponseRedirect('/')