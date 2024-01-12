from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm, CusOrdersUpd, CusRatFeedForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import CusOrders, CusRatingFeedback


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, 'Welcome {}, You have been successfully registerd'.format(username))
            form.save()
            return redirect('food:index')
    else:
        form = RegistrationForm()
        context = {
            'form':form
        }
        return render(request, 'users/register.html', context)
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(
                request,
                'Invalid login, try again'
            )
            return redirect('login_view')
        
        elif user.is_superuser:
            messages.success(
                request,
                '{}, is a superuser and has been successfully logged in'.format(username)
            )
            login(request, user)
            return redirect('food:index')
        
        elif user.is_authenticated:
            messages.success(
                request,
                '{}, you have been successfully logged in'.format(username)
            )
            login(request, user)
            return redirect('food:index')
        
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('food:index')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')

def Orders(requset, id, pdcd, user):

    context = {
        'pdcd':pdcd,
        'user':user
    }

    if requset.method == 'POST':

        Obj_CusOrds = CusOrders(
            prod_code=pdcd,
            user=user,
            quantity=requset.POST.get('qty')
        )

        Obj_CusOrds.save()

        return redirect('food:detail', item_id=id)

    return render(requset, 'users/orders.html', context)

def update_orders(request, id, upd_order_id):

    coo = CusOrders.objects.get(order_id=upd_order_id)
    form = CusOrdersUpd(request.POST or None, instance=coo)

    context = {
        'id':id,
        'upd_order_id':upd_order_id,
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('food:detail', item_id=id)

    return render(request, 'users/orders_upd.html', context)

def CusRatFeed(request, pc):
    
    form = CusRatFeedForm(request.POST or None)

    context = {
        'form':form,
        'pc':pc
    }

    if form.is_valid():
        form.instance.prod_code = pc
        form.instance.username = request.user.username
        form.instance.user_type = 'Cust'

        form.save()
        return redirect('food:index')

    return render(request, 'users/item-form.html', context)

def update_crf(request, details_id, crf_id):

    crfo = CusRatingFeedback.objects.get(id=crf_id)
    form = CusRatFeedForm(request.POST or None, instance=crfo)

    context = {
        'crfo':crfo,
        'form':form

    }

    if form.is_valid():
        form.save()
        return redirect('food:detail', item_id=details_id)
    
    return render(request, 'users/crf_upd.html', context)


def delete_crf(request, details_id, crf_id):
    crfo_del = CusRatingFeedback.objects.get(id=crf_id)

    context = {
        'crfo_del':crfo_del

    }

    if request.method == 'POST':
        crfo_del.delete()
        return redirect('food:detail', item_id=details_id)

    return render(request, 'users/crf_del.html', context)