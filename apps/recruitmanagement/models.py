from django.db import models

# Create your models here.
from django.utils import timezone


class RecruitManagement(models.Model):
    """
    招募管理表

    """
    # 社团名称
    club_id = models.SmallIntegerField(verbose_name='社团id')
    # 招新人数
    recruit_num = models.SmallIntegerField(verbose_name='招新人数')
    # 招新开始时间
    start_time = models.DateTimeField(verbose_name='开始时间', default=timezone.now)
    # 招新截止时间
    end_time = models.DateTimeField(verbose_name='截止时间')
    # 面试轮数
    interview_rounds = models.SmallIntegerField(verbose_name='面试轮数')
    # 邮件通知模板123