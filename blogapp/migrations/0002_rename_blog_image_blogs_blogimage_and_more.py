# Generated by Django 4.1 on 2022-09-02 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_image',
            new_name='blogimage',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_title',
            new_name='blogtitle',
        ),
        migrations.RenameField(
            model_name='blogs',
            old_name='related_file',
            new_name='relatedfile',
        ),
    ]