# Generated by Django 3.1.1 on 2020-11-14 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201113_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_joindate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
