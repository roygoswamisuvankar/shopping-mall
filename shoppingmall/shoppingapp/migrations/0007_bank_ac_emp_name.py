# Generated by Django 3.2.9 on 2022-03-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0006_bank_ac'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_ac',
            name='emp_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
