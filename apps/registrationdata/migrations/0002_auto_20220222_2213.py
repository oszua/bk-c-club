# Generated by Django 2.2.6 on 2022-02-22 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='resume_picture',
            field=models.ImageField(blank=True, null=True, upload_to='applicant_picture/', verbose_name='个人照片'),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='applicant_id',
            field=models.SmallIntegerField(verbose_name='简历id'),
        ),
        migrations.AlterField(
            model_name='registrationdata',
            name='club_id',
            field=models.SmallIntegerField(verbose_name='意向社团id'),
        ),
    ]
