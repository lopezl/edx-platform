EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'mooc@uji.es'
DEFAULT_FEEDBACK_EMAIL = 'mooc@uji.es'
SERVER_EMAIL = 'mooc@uji.es'
ADMINS = (
    ('edX Admins', 'lopezl@sg.uji.es'),
)
TIME_ZONE = 'Europe/Madrid'  # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
FORCE_SCRIPT_NAME = ''
#STATICFILES_DIRS = ('/opt/edx/static-cms',)