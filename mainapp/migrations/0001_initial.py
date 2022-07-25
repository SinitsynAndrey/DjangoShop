# Generated by Django 3.2.8 on 2021-10-30 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='название')),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('short_desc', models.CharField(blank=True, max_length=128, verbose_name='краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='колличество товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.products_categories')),
            ],
        ),
    ]
