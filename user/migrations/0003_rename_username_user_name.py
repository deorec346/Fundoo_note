# Generated by Django 4.0.5 on 2022-07-02 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_password_user_username_alter_user_email_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]
