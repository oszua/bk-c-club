from rest_framework import serializers

from apps.clubinfo.models import ClubInfo
from apps.registrationdata.models import RegistrationData, Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class RegistrationDataSerializer(serializers.ModelSerializer):
    club_info = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    def get_club_info(self, obj):
        """
        获取社团信息
        obj: 当前实例
        return: 当前社团信息
        """
        club_info = ClubInfo.objects.filter(id=obj.club_id).first()
        if club_info:
            return club_info.club_name
        else:
            return '无'

    def get_resume(self, obj):
        """
        获取简历信息
        obj: 当前实例
        return: 当前简历信息
        """
        resume = Resume.objects.filter(id=obj.resume_id).first()
        if resume:
            return resume.resume_name
        else:
            return '无'

    class Meta:
        model = RegistrationData
        fields = '__all__'

