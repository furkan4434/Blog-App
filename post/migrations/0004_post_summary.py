# Generated by Django 4.0.4 on 2022-06-11 16:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_b_context_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
