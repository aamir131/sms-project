# Generated by Django 3.1.6 on 2021-08-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0009_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
    ]
