# Generated by Django 3.1.14 on 2024-02-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0101_blog_ignored_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dashboard_footer',
            field=models.TextField(blank=True),
        ),
    ]
