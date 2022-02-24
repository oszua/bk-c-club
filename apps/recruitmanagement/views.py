from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.recruitmanagement.models import RecruitManagement
from apps.recruitmanagement.serializers import RecruitManagementSerializer


class RecruitManagementViewSet(viewsets.ModelViewSet):
    """
    增删改查招募信息
    """
    # 传入instance，关联数据库模型
    queryset = RecruitManagement.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = RecruitManagementSerializer


