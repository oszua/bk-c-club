from rest_framework.viewsets import ModelViewSet

from apps.registrationdata.models import RegistrationData
from apps.registrationdata.serializers import RegistrationDataSerializer
from common import viewsets
from common.pagination import DataPagePagination


class RegistrationDataViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查报名数据
    """
    queryset = RegistrationData.objects.all()
    serializer_class = RegistrationDataSerializer
    # 设置分页
    pagination_class = DataPagePagination


