# Generated by Django 3.2 on 2021-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210519_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
