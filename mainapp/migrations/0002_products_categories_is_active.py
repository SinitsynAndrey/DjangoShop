# Generated by Django 3.2.8 on 2021-11-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_categories',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]
