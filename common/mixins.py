import logging

from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from common import err_code


class ApiMixin(GenericViewSet):

    EXEMPT_STATUS_CODES = {status.HTTP_204_NO_CONTENT}

    def finalize_response(self, request, response, *args, **kwargs):
        # 对rest_framework的Response进行统一处理
        if isinstance(response, Response):
            if response.exception is True:
                error = response.data.get(
                    "detail", ErrorDetail("Error from API exception", err_code.UNKNOWN_ERROR.code)
                )
                response.data = {"result": False, "data": response.data, "code": error.code, "message": str(error)}
            elif response.status_code not in self.EXEMPT_STATUS_CODES:
                response.data = {"result": True, "data": response.data, "code": err_code.SUCCESS.code, "message": ""}

        return super(ApiMixin, self).finalize_response(request, response, *args, **kwargs)

