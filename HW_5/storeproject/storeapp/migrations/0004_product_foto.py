# Generated by Django 5.0.1 on 2024-02-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='foto',
            field=models.ImageField(default=None, upload_to='products/'),
        ),
    ]