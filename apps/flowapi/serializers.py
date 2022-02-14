from rest_framework import serializers

from engine.flowtmpl.models import FlowTmpl
from engine.flowtmpl.valid import FlowTmplTreeValidtor


class FlowTmplSerializer(serializers.ModelSerializer):

    tree = serializers.JSONField(
        validators=[FlowTmplTreeValidtor(),]
    )

    class Meta:
        model = FlowTmpl
        exclude = ["create_time", "creator", "editor"]
