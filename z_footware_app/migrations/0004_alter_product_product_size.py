# Generated by Django 5.1.1 on 2024-09-12 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_footware_app', '0003_product_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')], default=7),
        ),
    ]
