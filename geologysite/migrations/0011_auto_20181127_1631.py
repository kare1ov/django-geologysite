# Generated by Django 2.1.3 on 2018-11-27 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0010_auto_20181127_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.DeleteModel(
            name='RockModel',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
