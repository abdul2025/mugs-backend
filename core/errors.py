
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from enum import Enum
import logging
logger = logging.getLogger('django')

class Error(Enum):
    GENRAL_ERROR = {'code': 'General Customize Error as it goes', 'detail': _('{} ')}
    ILLEGAL_METHOD = {'code': 'This URL does not support the following HTTP method(s):', 'details': _('{} ')}

class APIError:

    """
    Format Error To match the STANDARD (response_data_formating)
        - Message = Our Error Enum
        - Error = Actual Error Exception
        - data = None
    """
    def __init__(self, error: Error, extra=None):
        self.error = error
        self.extra = extra or None
        error_detail = error.value
        if self.extra:
            # Extra values can be used in foramtting a string that contains {}
            if isinstance(self.extra, list):
                # Validate the extra is existed or return None

                error_detail['detail'] = {
                    'message': error.value['code'],
                    'error': self.extra,
                    'data': {
                           'details': None,
                        }
                    }
        try:
            logger.info(error.value)
        except BaseException:
            pass
        raise ValidationError(**error_detail)
