# Generated by Django 4.1 on 2024-05-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('vendor', models.CharField(max_length=64)),
                ('platform', models.CharField(max_length=64)),
                ('cost', models.FloatField()),
                ('renewal_date', models.DateField()),
                ('account_info', models.CharField(max_length=128)),
            ],
        ),
    ]