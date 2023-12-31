# Generated by Django 4.2 on 2023-08-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_purchased_plan_cancelled_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monthly_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quality', models.CharField(max_length=200)),
                ('resolution', models.CharField(max_length=200)),
                ('allow_devices', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Yearly_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('quality', models.CharField(max_length=200)),
                ('resolution', models.CharField(max_length=200)),
                ('allow_devices', models.CharField(max_length=200)),
            ],
        ),
    ]
