from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from apps.registrationdata.models import RegistrationData
from apps.registrationdata.serializers import RegistrationDataSerializer


class DataPagePagination(PageNumberPagination):

    # 设置每页显示条目为3条
    page_size = 3
    # 用户可以自定义选择一页的条数，但最多显示15条
    page_size_query_param = 'page_size'
    max_page_size = 15
    # 获取页码数
    page_query_param = 'page'


class RegistrationDataViewSet(viewsets.ModelViewSet):
    """
    增删改查报名数据
    """

    queryset = RegistrationData.objects.all()
    serializer_class = RegistrationDataSerializer
    # 设置分页
    pagination_class = DataPagePagination

