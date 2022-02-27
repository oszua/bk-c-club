from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet

from apps.clubinfo.models import ClubInfo
from apps.clubinfo.serializers import ClubInfoSerializer
from common import viewsets
# Create your views here.


class ClubInfoViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查社团信息
    """

    # 传入instance，关联数据库模型
    queryset = ClubInfo.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = ClubInfoSerializer
