# Generated by Django 2.1.3 on 2018-11-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0004_auto_20181120_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rockmodel',
            name='avatar',
            field=models.ImageField(upload_to='static/image'),
        ),
    ]
