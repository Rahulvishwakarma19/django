from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item, History
from food.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from users.models import CusOrders, CusRatingFeedback


# Create your views here.

# def index(request):
#     itemlist = Item.objects.all()
#     return HttpResponse(itemlist)


# function based index view
#------------------------------------------------------------------------
def index(request):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user=request.user.username)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

    else:
        itemlist = Item.objects.all()
    
    context = {
        'itemlist':itemlist

    }

    #return HttpResponse('This is an index view')
    return render(request, 'food/index.html', context)
# class based index view
#------------------------------------------------------------------------
class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'itemlist'

#function based detail view
#---------------------------------------------------------------------------
def detail(request, item_id):

    item = Item.objects.get(id=item_id)

    hist = History.objects.filter(
        prod_ref = item.prod_code
    )

    # restuarant and admin
    if request.user.profile.user_type == 'Rest' or request.user.profile.user_type == 'Admin':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code=item.prod_code
        )

    # customer
    elif request.user.profile.user_type == 'Cust':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code=item.prod_code,
            user=request.user.username
        )

    crf = CusRatingFeedback.objects.filter(
        prod_code=item.prod_code
    )


    context = {
        'item':item,
        'hist':hist,
        'oco' :Obj_CusOrd,
        'crf' :crf
    }
    return render(request, 'food/detail.html', context)

#class based detail view
#-------------------------------------------------------------------------------
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'
    context_object_name = 'item'

def item(request):
    return HttpResponse('<h1 style="color:red">This is an item</h1>')

#funtion based create_item view
#------------------------------------------------------------------------------
def create_item(request):
    form = ItemForm(request.POST or None)

    context = {
        'form':form

    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context)

# class based detail create_item view
#-----------------------------------------------------------------------------
class CreateItem(CreateView):
    model = Item
    fields = ['prod_code','for_user','item_name', 'item_desc', 'item_image', 'item_price']
    template_name = 'food/item-form.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        obj_History = History(
            user_name = self.request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = self.request.POST['item_name'],
            op_type = 'Created'

        )

        obj_History.save()


        return super().form_valid(form)
# function based update item view
#------------------------------------------------------------------------------
def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'item':item,
        'form':form
    }

    if form.is_valid():
        form.save()


        obj_History = History(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = request.POST['item_name'],
            op_type = 'Updated'

        )

        obj_History.save()

        return redirect('food:index')
    
    return render(request, 'food/item-form.html', context)

# function based delete item view
#-------------------------------------------------------------------------------
def delete_item(request, id):
    item = Item.objects.get(pk=id)

    context = {
        'item':item
    }

    if request.method == "POST":

        obj_History = History(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'

        )

        obj_History.save()

        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', context)


# def item(request):
#     return HttpResponse('<h1 style="color:red">This is an item</h1>')

    # context = {
    #     'value':7
    # }

    # return render(request, 'food/detail.html', context)    
