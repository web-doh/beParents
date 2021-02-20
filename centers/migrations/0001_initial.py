# Generated by Django 3.1.1 on 2020-11-14 04:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=100, null=True)),
                ('center_type', models.CharField(max_length=100, null=True)),
                ('center_phone', models.CharField(max_length=100, null=True)),
                ('center_address', models.CharField(max_length=100, null=True)),
                ('homepage', models.CharField(max_length=200, null=True)),
                ('runhours', models.CharField(max_length=200, null=True)),
                ('hashtags', models.JSONField(default=list, null=True)),
                ('content_urls', models.JSONField(default=list, null=True)),
                ('contents', models.JSONField(default=list, null=True)),
                ('x', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('y', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'centers_center_review_users',
            },
        ),
        migrations.CreateModel(
            name='CenterReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('score', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='centers')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centers.center')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CenterLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centers.center')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='center',
            name='like_users',
            field=models.ManyToManyField(null=True, related_name='like_centers', through='centers.CenterLike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='center',
            name='review_users',
            field=models.ManyToManyField(null=True, related_name='review_centers', through='centers.CenterReview', to=settings.AUTH_USER_MODEL),
        ),
    ]