from django.urls import path
from food import views

app_name = 'food'
urlpatterns = [

    # function based index view
    path('home/', views.index, name='index'),

    # class based index view
    #path('home/', views.IndexClassView.as_view(), name='index'),



    #path('item/', views.item, name='item'),

    #funtion based detail view
    path('<int:item_id>/', views.detail, name='detail'),

    #classed based detail view
    #path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),

    #function based create_item view
    #path('add/', views.create_item, name='create_item'),

    #class based create_item view
    path('add/', views.CreateItem.as_view(), name='create_item'),
    
    path('update/<int:id>/', views.update_item, name='update_item'),

    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]
