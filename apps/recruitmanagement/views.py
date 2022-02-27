from rest_framework.viewsets import ModelViewSet
from apps.recruitmanagement.models import RecruitManagement
from apps.recruitmanagement.serializers import RecruitManagementSerializer
from common import viewsets


class RecruitManagementViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查招募信息
    """
    # 传入instance，关联数据库模型
    queryset = RecruitManagement.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = RecruitManagementSerializer


