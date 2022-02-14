
class ErrorCode(object):
    def __init__(self, code, description, ignore_prefix=False):
        self.code = int(code) if ignore_prefix else int(f"{code}")
        self.description = description

    def __str__(self):
        return self.code


SUCCESS = ErrorCode(code="0", description="success", ignore_prefix=True)

REQUEST_PARAM_INVALID = ErrorCode(code="40000", description="the content of param in your request is invalid")
REQUEST_FORBIDDEN_INVALID = ErrorCode(code="40100", description="you have no permission")
CONTENT_NOT_EXIST = ErrorCode(code="40400", description="the content you reqeust does not exist")
INVALID_OPERATION = ErrorCode(code="45000", description="invalid operation")
OPERATION_FAIL = ErrorCode(code="45100", description="invalid operation")
VALIDATION_ERROR = ErrorCode(code="46100", description="validation error")

ENV_ERROR = ErrorCode(code="55000", description="environment error")

UNKNOWN_ERROR = ErrorCode(code="99999", description="unknow error")