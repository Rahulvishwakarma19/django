# Generated by Django 4.2.3 on 2023-08-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.vandeoorsprong.com/wp-content/uploads/2019/07/Placeholder-food-2.jpg', max_length=500),
        ),
    ]