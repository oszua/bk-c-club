import jsonfield

from django.db import models


class FlowTmpl(models.Model):
    name = models.CharField(verbose_name="流程模板名称", max_length=32)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_created=True)
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    creator = models.CharField(verbose_name="创建人", max_length=32)
    editor = models.CharField(verbose_name="修改人", max_length=32)
    tree =  jsonfield.JSONField(verbose_name="流程模板树")
    
