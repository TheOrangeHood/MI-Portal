# Generated by Django 4.0.3 on 2022-03-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_coordieassignedtask_cg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordieassignedtask',
            name='cg',
            field=models.TextField(max_length=30),
        ),
    ]
