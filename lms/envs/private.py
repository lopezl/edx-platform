from .common import ENV_ROOT
from logsettings import get_logger_config

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

MKTG_URL_LINK_MAP = {
    'ABOUT': 'about_edx',
    'CONTACT': 'contact',
    'FAQ': 'faq_edx',
    'COURSES': 'courses',
    'ROOT': 'root',
    'TOS': 'tos',
    'HONOR': 'honor',
    'PRIVACY': 'privacy_edx',
}

DEFAULT_FROM_EMAIL = 'mooc@uji.es'
DEFAULT_FEEDBACK_EMAIL = 'mooc@uji.es'
SERVER_EMAIL = 'mooc@uji.es'
TECH_SUPPORT_EMAIL = 'mooc@uji.es'
CONTACT_EMAIL = 'mooc@uji.es'
BUGS_EMAIL = 'mooc@uji.es'
ADMINS = (
    ('edX Admins', 'lopezl@sg.uji.es'),
)

FAVICON_PATH = 'images/uji.ico'

# Locale/Internationalization
TIME_ZONE = 'Europe/Madrid'  # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
FORCE_SCRIPT_NAME = ''

#UJI: from lms/envs/common.py modifications
SITE_NAME = "mooc.uji.es"
HTTPS = 'no'

COMMENTS_SERVICE_KEY = "pepito"
COMMENTS_SERVICE_URL = "http://localhost:8082/"

DEBUG = True
TEMPLATE_DEBUG = True

LOGGING = get_logger_config(ENV_ROOT / "log",
                            logging_env="uji",
                            local_loglevel="DEBUG",
                            dev_env=False,
                            debug=True)
 
