# Generated by Django 3.2 on 2021-06-22 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_faq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(max_length=255),
        ),
    ]