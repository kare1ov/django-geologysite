# Generated by Django 2.1.3 on 2018-12-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geologysite', '0014_article_date_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='rockmodel',
            name='field_task3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
