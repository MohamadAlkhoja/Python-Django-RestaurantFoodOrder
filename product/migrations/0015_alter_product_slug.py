# Generated by Django 3.2 on 2021-06-17 21:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]