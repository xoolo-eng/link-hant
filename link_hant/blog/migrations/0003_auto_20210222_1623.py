# Generated by Django 3.1.5 on 2021-02-22 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210215_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-create', '-id'), 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'ordering': ('name',), 'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
    ]
