# Generated by Django 3.1.1 on 2020-11-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerreview',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='centers'),
        ),
    ]
