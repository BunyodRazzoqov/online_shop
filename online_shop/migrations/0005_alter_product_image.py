# Generated by Django 5.0.7 on 2024-07-30 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0004_alter_product_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
