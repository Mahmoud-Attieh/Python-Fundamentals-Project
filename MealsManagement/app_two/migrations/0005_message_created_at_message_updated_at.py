# Generated by Django 4.2.1 on 2023-06-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-06-15 11:59:10.377292'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
