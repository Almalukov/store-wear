# Generated by Django 4.2.4 on 2023-08-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
