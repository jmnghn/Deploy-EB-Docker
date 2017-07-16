# debug.py
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 디버그모드니까 DEBUG는 True
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

print('@@@@@@ DEBUG:', DEBUG)
print('@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)