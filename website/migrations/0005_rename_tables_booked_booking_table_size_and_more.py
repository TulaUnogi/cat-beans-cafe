# Generated by Django 4.2.7 on 2023-11-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_customer_userprofile_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='tables_booked',
            new_name='table_size',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.CharField(choices=[('8:00 - 8:30', '8:00 - 8:30'), ('8:30 - 9:00', '8:30 - 9:00'), ('9:00 - 9:30', '9:00 - 9:30'), ('9:30 - 10:00', '9:30 - 10:00'), ('10:00 - 10:30', '10:00 - 10:30'), ('10:30 - 11:00', '10:30 - 11:00'), ('11:00 - 11:30', '11:00 - 11:30'), ('11:30 - 12:00', '11:30 - 12:00'), ('12:00 - 12:30', '12:00 - 12:30'), ('12:30 - 13:00', '12:30 - 13:00'), ('13:00 - 13:30', '13:00 - 13:30'), ('13:30 - 14:00', '13:30 - 14:00'), ('14:00 - 14:30', '14:00 - 14:30'), ('14:30 - 15:00', '14:30 - 15:00'), ('15:00 - 15:30', '15:00 - 15:30'), ('15:30 - 16:00', '15:30 - 16:00'), ('16:00 - 16:30', '16:00 - 16:30'), ('16:30 - 17:00', '16:30 - 17:00')], default='8:00 - 8:30', max_length=50),
        ),
    ]
