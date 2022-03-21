# Generated by Django 4.0.3 on 2022-03-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordieAssignedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordieEmail', models.EmailField(max_length=30)),
                ('coordieTask', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='CoordieTask',
        ),
    ]
