# Generated by Django 3.1.1 on 2021-04-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_trades', models.IntegerField()),
                ('loss_trades', models.IntegerField()),
                ('date_of_trade', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
                ('item_code', models.IntegerField()),
                ('item_condition', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
