# Generated by Django 4.2.3 on 2023-10-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CusOrders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_code', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]