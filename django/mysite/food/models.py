from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name
        #return self.item_desc
        #return str(self.item_price)

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=200, default='Alex')
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=300, default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis quasi magni, consequuntur aliquam eveniet, nihil temporibus nam voluptatem, eaque fugit illum id adipisci sapiente repellat delectus? Eius nostrum debitis officia!')
    item_price = models.IntegerField()
    item_image= models.CharField(max_length=500, default='https://www.vandeoorsprong.com/wp-content/uploads/2019/07/Placeholder-food-2.jpg')


class History(models.Model):
    def __str__(self):
        return str(
            (
                self.prod_ref,
                self.user_name,
                self.item_name,
                self.op_type
            )
        ) 
    
    user_name = models.CharField(max_length=200)
    prod_ref = models.IntegerField(default=100)
    item_name = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)
    

