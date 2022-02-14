from rest_framework import mixins, status
from rest_framework.response import Response

from common import viewsets
from apps.flowapi.serializers import FlowTmplSerializer


class FlowTmplViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

    serializer_class = FlowTmplSerializer

    def create(self, request, *args, **kwargs):
        creator = request.user.username
        editor = request.user.username
        data = request.data.copy()
        data["creator"] = creator
        data["editor"] = editor
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
