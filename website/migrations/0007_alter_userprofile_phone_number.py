# Generated by Django 4.2.7 on 2023-11-30 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_booking_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.IntegerField(max_length=17),
        ),
    ]
