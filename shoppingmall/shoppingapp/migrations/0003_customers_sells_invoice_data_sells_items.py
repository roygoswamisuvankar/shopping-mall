# Generated by Django 3.2.9 on 2022-02-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0002_add_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='customers_sells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=14, null=True)),
                ('inv_no', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('gtotal', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='invoice_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_no', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('gtotal', models.IntegerField(max_length=50)),
                ('emp_id', models.IntegerField(max_length=50)),
                ('emp_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='sells_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('pro_name', models.CharField(max_length=50)),
                ('qty', models.IntegerField(max_length=20)),
                ('mrp', models.IntegerField(max_length=20)),
                ('unit', models.CharField(max_length=30)),
                ('discount', models.IntegerField(max_length=20)),
                ('amount', models.IntegerField(max_length=10)),
                ('date', models.DateField(max_length=50)),
                ('inv_no', models.CharField(max_length=50)),
            ],
        ),
    ]
