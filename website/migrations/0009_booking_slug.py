# Generated by Django 4.2.7 on 2023-11-30 16:53

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=70, null=True, unique=True),
        ),
    ]