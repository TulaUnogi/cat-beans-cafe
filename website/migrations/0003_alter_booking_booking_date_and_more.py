# Generated by Django 4.2.7 on 2023-11-27 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_auto_20231118_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.IntegerField(choices=[(0, '8:00 - 8:30'), (1, '8:30 - 9:00'), (2, '9:00 - 9:30'), (3, '9:30 - 10:00'), (4, '10:00 - 10:30'), (5, '10:30 - 11:00'), (6, '11:00 - 11:30'), (7, '11:30 - 12:00'), (8, '12:00 - 12:30'), (9, '12:30 - 13:00'), (10, '13:00 - 13:30'), (11, '13:30 - 14:00'), (12, '14:00 - 14:30'), (13, '14:30 - 15:00'), (17, '15:00 - 15:30'), (18, '15:30 - 16:00'), (19, '16:00 - 16:30'), (20, '16:30 - 17:00')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tables_booked',
            field=models.IntegerField(choices=[(1, 'Single window seat'), (2, 'Small- 2 seats'), (4, 'Medium- 4 seats'), (6, 'Large- 6 seats')], default=0),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=17)),
                ('email', models.EmailField(max_length=300)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.userprofile'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]