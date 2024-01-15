from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm, TestForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from django.urls import reverse_lazy

# Create your views here.
def index(request): 
    return render(request, 'main/index.html')

def auth(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/lobby')
                else:
                    return HttpResponse('Disabled account')
            else:
                print('Access denied')
                return render(request, 'main/login.html', {'form': form, 'access_denied': True})
        else: 
            print(form.errors)
    else:
        form = LoginUserForm()

    return render(request, 'main/auth.html', {'form': form})   

@login_required(login_url='/register')
def test(request): 


    if request.method == 'POST':

        form = TestForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else: 
            print(form.errors)
    else:
        form = RegisterUserForm()  

    return render(request, 'main/test.html', {'form': TestForm})

def registration(request): 
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.first_name = user_form.cleaned_data['name']
            user.save()
            user_acc = UserAccount(user=user)
            user_acc.save()
            login(request, user)
            return redirect('/lobby')
    else:
        user_form = RegisterUserForm()  
    return render(request, 'main/registration.html', {'form': user_form})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_1(request): 
    next_page = 2
    return render(request, 'main/page_1.html', {'page_num': next_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_2(request): 
    next_page = 3
    prev_page = 1
    return render(request, 'main/page_2.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_3(request): 
    next_page = 4
    prev_page = 2
    return render(request, 'main/page_3.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_4(request): 
    next_page = 5
    prev_page = 3
    return render(request, 'main/page_4.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_5(request): 
    next_page = 6
    prev_page = 4
    return render(request, 'main/page_5.html', {'page_num': next_page, "prev_page": prev_page})

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def page_6(request): 
    next_page = 6
    prev_page = 5
    return render(request, 'main/page_6.html', {'page_num': next_page, "prev_page": prev_page})

def bad_res(request): 
    return render(request, 'main/test.html')

def good_res(request): 
    return render(request, 'main/test.html')

@login_required(login_url=reverse_lazy('main:auth'), redirect_field_name=None)
def lobby(request): 
    return render(request, 'main/lobby.html')


def logout_user(request):
    logout(request)
    return redirect('/auth')