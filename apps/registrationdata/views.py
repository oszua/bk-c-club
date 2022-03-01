from rest_framework.viewsets import ModelViewSet

from apps.registrationdata.models import RegistrationData
from apps.registrationdata.serializers import RegistrationDataSerializer
from common import viewsets
from common.pagination import DataPagePagination


class RegistrationDataViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查报名数据

    list:
    返回报名数据列表

    create:
    创建报名数据

    retrieve:
    返回指定报名数据

    update:
    更新报名信息

    partial_update:
    更新部分字段

    destroy:
    删除指定报名数据

    """
    queryset = RegistrationData.objects.all()
    serializer_class = RegistrationDataSerializer
    # 设置分页
    pagination_class = DataPagePagination


