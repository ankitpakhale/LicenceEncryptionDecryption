# Generated by Django 4.0.3 on 2022-06-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_app', '0005_alter_li_model_licence_no_alter_seller_detail_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_detail',
            name='age',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
