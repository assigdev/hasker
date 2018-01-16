from .base import *
from .other_conf import *
from .apps_conf import *


try:
    from .local_settings import *

    RAVEN_CONFIG = {
        'dsn': 'https://63ba3f0edeb1469cbd3714b08f699e8d:cf5207a6860c4766994d1e120fa3add3@sentry.io/250939',
    }
except ImportError:
    from .dev import *
    # INSTALLED_APPS += ['sslserver']
    # INSTALLED_APPS += ['debug_toolbar']
    # MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    # INTERNAL_IPS = ['127.0.0.1']
    # DEBUG_TOOLBAR_PANELS = [
    #     'debug_toolbar.panels.versions.VersionsPanel',
    #     'debug_toolbar.panels.timer.TimerPanel',
    #     'debug_toolbar.panels.settings.SettingsPanel',
    #     'debug_toolbar.panels.headers.HeadersPanel',
    #     'debug_toolbar.panels.request.RequestPanel',
    #     'debug_toolbar.panels.sql.SQLPanel',
    #     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    #     'debug_toolbar.panels.templates.TemplatesPanel',
    #     'debug_toolbar.panels.cache.CachePanel',
    #     'debug_toolbar.panels.signals.SignalsPanel',
    #     'debug_toolbar.panels.logging.LoggingPanel',
    #     'debug_toolbar.panels.redirects.RedirectsPanel',
    #     # 'debug_toolbar.panels.profiling.ProfilingPanel',
    # ]
    #
    # DEBUG_TOOLBAR_CONFIG = {
    #     'INTERCEPT_REDIRECTS': False,
    # }
