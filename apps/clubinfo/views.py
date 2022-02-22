from django.shortcuts import render
from rest_framework import viewsets
from apps.clubinfo.models import ClubInfo
from apps.clubinfo.serializers import ClubInfoSerializer

# Create your views here.



class ClubInfoViewSet(viewsets.ModelViewSet):
    """
    增删改查图书信息
    """

    # 传入instance，关联数据库模型
    queryset = ClubInfo.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = ClubInfoSerializer