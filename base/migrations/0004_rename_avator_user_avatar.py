# Generated by Django 4.2.3 on 2023-07-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avator',
            new_name='avatar',
        ),
    ]
