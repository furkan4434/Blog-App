# Generated by Django 4.0.4 on 2022-06-11 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_b_context'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='b_context',
            new_name='description',
        ),
    ]
