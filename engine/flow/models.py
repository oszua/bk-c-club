import jsonfield

from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from engine.flowtmpl.models import FlowTmpl
from engine.flow.dispatcher import FlowDispatcher

class FlowManager(models.Manager):
    def create(self,**kwargs):
        # 构造流程
        template_id = kwargs["template_id"]
        try:
            template = FlowTmpl.objects.get(id=template_id)
        except ObjectDoesNotExist:
            return None
        tree = template.tree
        creator = kwargs["creator"]
        editor = kwargs.get("editor", creator)
        student_id = kwargs["student_id"]
        club_id = kwargs["club_id"]
        pipeline = FlowDispatcher.build_pipeline(tree, student_id, club_id)
        flow = super().create(
            creator=creator,editor=editor,pipeline=pipeline
        )
        flow.save()
        return flow

class Flow(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_created=True)
    edit_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)
    creator = models.CharField(verbose_name="创建者",max_length=32)
    editor = models.CharField(verbose_name="修改人", max_length=32)
    pipeline =  jsonfield.JSONField(verbose_name="流程实例")

    objects = FlowManager()
