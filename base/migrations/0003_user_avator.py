# Generated by Django 4.2.3 on 2023-07-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avator',
            field=models.ImageField(default='avator.svg', null=True, upload_to=''),
        ),
    ]
