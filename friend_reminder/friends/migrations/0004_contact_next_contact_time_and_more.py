# Generated by Django 4.0.2 on 2022-02-13 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_availablecontacttime_day_of_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='next_contact_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='next_contact_date',
            field=models.DateField(),
        ),
    ]
