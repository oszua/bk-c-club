# Generated by Django 2.2.6 on 2022-02-24 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registrationdata', '0002_auto_20220222_2213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationdata',
            old_name='applicant_id',
            new_name='resume_id',
        ),
    ]