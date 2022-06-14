# Generated by Django 4.0.3 on 2022-06-11 09:55

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('l_app', '0002_rename_seller_name_li_model_seller_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_detail',
            name='email',
            field=django_cryptography.fields.encrypt(models.EmailField(max_length=100)),
        ),
    ]
