from django.db import models

# Create your models here.


class Resume (models.Model):
    """
    个人简历表
    """
    # 报名者姓名
    resume_name = models.CharField(max_length=10, verbose_name='姓名')
    # 报名者性别
    gender = models.IntegerField(choices=((1, "男"), (2, "女")), verbose_name='性别', default=0)
    # # 个人照片：待处理方案照片上传
    resume_picture = models.ImageField(upload_to='applicant_picture/', verbose_name='个人照片', null=True, blank=True)
    # 学院
    institute = models.CharField(max_length=50, verbose_name='学院')
    # 专业
    major = models.CharField(max_length=30, verbose_name='专业')
    # 手机号
    phone_num = models.CharField(max_length=11, verbose_name='手机号', unique=True)
    # 邮箱地址
    email = models.EmailField(verbose_name='邮箱', unique=True)
    # qq号
    qq = models.CharField(max_length=11, verbose_name='qq', unique=True)
    # 自我介绍(200字以内)
    self_introduction = models.CharField(max_length=200, verbose_name='自我介绍')

    class Meta:
        verbose_name = "个人简历表"
        verbose_name_plural = verbose_name
        # 建立联合约束：避免简历重复创建
        unique_together = ("resume_name", "phone_num", "qq")


class RegistrationData(models.Model):
    """
    报名数据表(个人简历与社团关系)
    """
    # 报名者姓名(绑定简历id)
    applicant_id = models.SmallIntegerField(verbose_name='简历id')
    # 意向社团
    club_id = models.SmallIntegerField(verbose_name='意向社团id')
    # 第一意向部门及第二意向部门
    first_department = models.CharField(max_length=16, verbose_name='第一意向部门')
    second_department = models.CharField(max_length=16, verbose_name='第二意向部门')
    # 投递时间排序
    create_time = models.DateTimeField(auto_now_add=True)
    # 当前所处状态,
    current = models.SmallIntegerField(verbose_name='当前状态')

    class Meta:
        ordering=['-create_time']