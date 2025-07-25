# Generated by Django 5.2.4 on 2025-07-21 06:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='short_description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
