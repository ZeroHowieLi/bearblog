# Generated by Django 4.0.4 on 2022-08-03 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0063_remove_blog_external_stylesheet_alter_blog_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]