# Generated by Django 3.2.9 on 2021-12-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_shopuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='url_avatar',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]