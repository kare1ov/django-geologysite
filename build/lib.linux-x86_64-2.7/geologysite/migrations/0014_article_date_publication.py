# Generated by Django 2.1.3 on 2018-12-13 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0013_auto_20181201_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date_publication',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]