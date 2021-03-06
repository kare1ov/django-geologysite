# Generated by Django 2.1.3 on 2018-11-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0006_auto_20181122_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineralmodel',
            name='avatar',
            field=models.ImageField(upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='mineralmodel',
            name='density',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mineralmodel',
            name='hardness',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='rockmodel',
            name='avatar',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
