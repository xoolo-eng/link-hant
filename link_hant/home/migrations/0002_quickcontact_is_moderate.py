# Generated by Django 3.1.5 on 2021-02-10 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickcontact',
            name='is_moderate',
            field=models.BooleanField(default=False, verbose_name='Is moderations'),
        ),
    ]
