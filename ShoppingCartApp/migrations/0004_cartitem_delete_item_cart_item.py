# Generated by Django 4.0.4 on 2022-04-19 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCartApp', '0003_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(blank=True, to='ShoppingCartApp.cartitem'),
        ),
    ]