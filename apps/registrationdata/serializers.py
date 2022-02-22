from rest_framework import serializers

from apps.registrationdata.models import RegistrationData, Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"


class RegistrationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationData
        fields = '__all__'
