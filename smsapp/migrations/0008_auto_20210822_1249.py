# Generated by Django 3.1.6 on 2021-08-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0007_auto_20210723_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
    ]
