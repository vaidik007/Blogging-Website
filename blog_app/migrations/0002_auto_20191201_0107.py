# Generated by Django 2.2.5 on 2019-11-30 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_post',
            old_name='Post_Titile',
            new_name='Post_Title',
        ),
    ]
