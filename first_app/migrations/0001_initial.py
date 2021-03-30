# Generated by Django 2.1 on 2021-03-06 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=50)),
                ('areamember', models.CharField(default='satya', max_length=100)),
                ('areacode', models.IntegerField()),
                ('areadistrict', models.CharField(default='HYD', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('salary', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.Department')),
            ],
        ),
    ]
