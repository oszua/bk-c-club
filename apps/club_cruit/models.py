from django.db import models

# Create your models here.
class RecruitManagement(models.Model):

    club_id = models.IntegerField(verbose_name="社团id")
    num = models.CharField(verbose_name="招募人数", max_length=10)
    qq = models.CharField(max_length=50, null=True, blank=True, verbose_name="招新qq群")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = "社团招募表"
        verbose_name_plural = verbose_name