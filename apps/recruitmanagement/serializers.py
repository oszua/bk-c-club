from rest_framework import serializers

from apps.clubinfo.models import ClubInfo
from apps.recruitmanagement.models import RecruitManagement


class RecruitManagementSerializer(serializers.ModelSerializer):
    club_info = serializers.SerializerMethodField()

    def get_club_info(self, obj):
        """
        获取社团信息
        obj: 当前实例
        return: 当前社团信息
        """
        club_info = ClubInfo.objects.filter(id=obj.club_id).first()
        return club_info

    class Meta:
        model = RecruitManagement
        fields = '__all__'

