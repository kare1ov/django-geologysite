# Generated by Django 2.1.3 on 2018-11-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0003_auto_20181119_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineralmodel',
            name='avatar',
            field=models.ImageField(upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='rockmodel',
            name='avatar',
            field=models.ImageField(default='', upload_to='static/image'),
        ),
    ]