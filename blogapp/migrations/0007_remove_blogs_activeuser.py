# Generated by Django 4.1 on 2022-09-03 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_blogs_activeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='activeuser',
        ),
    ]