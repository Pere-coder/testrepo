# Generated by Django 4.1 on 2022-08-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
