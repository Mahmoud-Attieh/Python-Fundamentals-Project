# Generated by Django 4.2.1 on 2023-06-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_company_company_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=45)),
                ('submitcomplain', models.CharField(max_length=250)),
            ],
        ),
    ]
