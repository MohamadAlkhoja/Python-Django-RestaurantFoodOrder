# Generated by Django 3.2 on 2021-06-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]