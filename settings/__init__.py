from .base import *
from ._installed_apps import *
from ._app_virables import *

IS_PRODUCTION = os.getenv('PRODUCTION', False)

if IS_PRODUCTION:
    from .prod import *
else:
    from .dev import *
