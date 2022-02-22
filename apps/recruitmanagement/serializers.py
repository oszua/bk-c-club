from rest_framework import serializers

from apps.recruitmanagement.models import RecruitManagement


class RecruitManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitManagement
        fields = '__all__'