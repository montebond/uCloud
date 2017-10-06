# -*- coding: utf-8 -*-
from .base import *

# Required function for Heroku to parse the DB variables
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = [
                '127.0.0.1',
                'www.ucloud.live',
                'ucloud.live',
                'ucloud-live.herokuapp.com',
                'discover.ucloud.live',
                'journey.ucloud.live',
                'finance.ucloud.live',
                'health.ucloud.live',
                'education.ucloud.live',
                ]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

#Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
