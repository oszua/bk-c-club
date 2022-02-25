from django.forms import model_to_dict
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
        club = obj
        club_info = ClubInfo.objects.filter(id=club.club_id).first()
        if club_info:
            return club_info.club_name
        else:
            return '无'

    class Meta:
        model = RecruitManagement
        fields = '__all__'

