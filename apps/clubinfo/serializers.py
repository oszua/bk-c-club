from rest_framework import serializers

from apps.clubinfo.models import ClubInfo


class ClubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubInfo
        fields = '__all__'