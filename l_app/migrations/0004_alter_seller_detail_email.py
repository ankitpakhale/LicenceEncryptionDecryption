# Generated by Django 4.0.3 on 2022-06-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_app', '0003_alter_seller_detail_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller_detail',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
