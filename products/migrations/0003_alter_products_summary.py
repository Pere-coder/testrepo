# Generated by Django 4.1 on 2022-08-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]