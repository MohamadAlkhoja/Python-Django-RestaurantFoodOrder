# Generated by Django 3.2 on 2021-06-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tableno',
            field=models.IntegerField(blank=True, max_length=20),
        ),
    ]
