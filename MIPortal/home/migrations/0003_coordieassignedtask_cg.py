# Generated by Django 4.0.3 on 2022-03-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_coordieassignedtask_delete_coordietask'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordieassignedtask',
            name='cg',
            field=models.TextField(default='admin', max_length=30),
        ),
    ]
