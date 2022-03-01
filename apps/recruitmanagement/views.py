from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from apps.recruitmanagement.models import RecruitManagement
from apps.recruitmanagement.serializers import RecruitManagementSerializer
from common import viewsets

# 使列表视图api不显示在自动生成的api文档中
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        auto_schema=None,
    ),
)
class RecruitManagementViewSet(viewsets.GenericViewSet, ModelViewSet):
    """
    增删改查招募信息

    create:
    创建社团招募信息

    retrieve:
    返回指定社团招募信息

    update:
    更新社团招募信息

    partial_update:
    更新部分字段

    destroy:
    删除社团招募信息


    """
    # 传入instance，关联数据库模型
    queryset = RecruitManagement.objects.all()
    # 传入serializer，关联序列化器
    serializer_class = RecruitManagementSerializer


