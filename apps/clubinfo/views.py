from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from apps.clubinfo.models import ClubInfo
from apps.clubinfo.serializers import ClubInfoSerializer
from common import viewsets
# Create your views here.

# 使列表视图api不显示在自动生成的api文档中
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        auto_schema=None,
    ),
)
class ClubInfoViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查社团信息

    create:
    创建社团

    retrieve:
    返回指定社团信息

    update:
    更新社团信息

    partial_update:
    更新部分字段

    destroy:
    删除社团
    """

    # 传入instance，关联数据库模型
    queryset = ClubInfo.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = ClubInfoSerializer
