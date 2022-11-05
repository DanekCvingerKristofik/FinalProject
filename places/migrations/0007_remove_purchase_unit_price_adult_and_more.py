# Generated by Django 4.1.1 on 2022-11-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_purchase_unit_price_adult_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='unit_price_adult',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='unit_price_child',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount_adults',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount_children',
            field=models.IntegerField(),
        ),
    ]