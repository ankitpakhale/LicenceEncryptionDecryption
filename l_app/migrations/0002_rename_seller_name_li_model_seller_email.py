# Generated by Django 4.0.3 on 2022-06-11 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('l_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='li_model',
            old_name='seller_name',
            new_name='seller_email',
        ),
    ]
