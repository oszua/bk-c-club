from django.db import models

# Create your models here.


class ClubInfo(models.Model):
    """
    社团信息表
    """
    # 社团名称(名称唯一不重复)
    club_name = models.CharField(max_length=30, unique=True, verbose_name='社团名称')
    # 社团简介（不限制字数）
    introduction = models.TextField(verbose_name='社团简介')
    # 社团拥有的部门
    department = models.CharField(max_length=256, verbose_name='拥有部门')
    # 社团logo(设置上传路径): 待处理方案照片上传
    logo = models.ImageField(upload_to='logo/', verbose_name='logo', null=True, blank=True)
    # # 社团精彩集锦(上传路径)
    club_picture = models.ImageField(upload_to='club_picture/', verbose_name='社团活动照', null=True, blank=True)
    # 招新qq群二维码(待定)
    # 招新微信群二维码

    class Meta:
        verbose_name = "社团信息表"
        verbose_name_plural = verbose_name
        # 建立联合约束，防止重复创建
        unique_together = ("club_name", "logo")