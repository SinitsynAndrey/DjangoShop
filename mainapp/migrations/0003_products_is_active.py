# Generated by Django 3.2.8 on 2021-11-24 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_products_categories_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]