import os

SITE_DIR = os.path.dirname( os.path.abspath( __file__) )
BASE_DIR = os.path.dirname( SITE_DIR )

SITE_ID = 1

# Memory Settings
# 50MB for POST data
DATA_UPLOAD_MAX_MEMORY_SIZE = 52428800
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o2775
FILE_UPLOAD_PERMISSIONS = 0o664

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'MY_SECRET_KEY_IS_VERY_LONG_WHY_DONT_YOU_LOOK_AT_IT!?LOOK-AT-IT!!'

# Application definition
SESSION_ENGINE = "redis_sessions.session"

INSTALLED_APPS = (
	'djangocms_admin_style'
	, 'django.contrib.admin'
	, 'django.contrib.auth'
	, 'django.contrib.contenttypes'
	, 'django.contrib.sessions'
	, 'django.contrib.messages'
	, 'django.contrib.staticfiles'
	, 'django.contrib.sites'
	, 'django.contrib.sitemaps'
	, 'cms'
	, 'menus'
	, 'treebeard'
	, 'sekizai'
	, 'app0'
)

MIDDLEWARE = (
	'django.middleware.common.CommonMiddleware'
	, 'django.middleware.csrf.CsrfViewMiddleware'
	, 'django.contrib.sessions.middleware.SessionMiddleware'
	, 'django.contrib.auth.middleware.AuthenticationMiddleware'
	, 'django.contrib.messages.middleware.MessageMiddleware'
	, 'django.middleware.clickjacking.XFrameOptionsMiddleware'
	, 'django.middleware.security.SecurityMiddleware'
	, 'django.middleware.locale.LocaleMiddleware'
	, 'cms.middleware.utils.ApphookReloadMiddleware'
	, 'cms.middleware.user.CurrentUserMiddleware'
	, 'cms.middleware.page.CurrentPageMiddleware'
	, 'cms.middleware.toolbar.ToolbarMiddleware'
	, 'cms.middleware.language.LanguageCookieMiddleware'
)

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
	'easy_thumbnails.processors.colorspace'
	, 'easy_thumbnails.processors.autocrop'
	, 'filer.thumbnail_processors.scale_and_crop_with_subject_location'
	, 'easy_thumbnails.processors.filters'
)

ROOT_URLCONF = 'app0.urls'

TEMPLATES = [ {
	'BACKEND': 'django.template.backends.django.DjangoTemplates'
	, 'DIRS': [ 'templates' ]
	, 'APP_DIRS': True
	, 'OPTIONS': {
		'context_processors': [
			'django.template.context_processors.debug'
			, 'django.template.context_processors.request'
			, 'django.contrib.auth.context_processors.auth'
			, 'django.contrib.messages.context_processors.messages'
			, 'sekizai.context_processors.sekizai'
			, 'cms.context_processors.cms_settings'
		]
	}
} ]

CMS_TOOLBAR_ANONYMOUS_ON = False
CMS_TEMPLATES = [
	( 'app0/BASS.html', 'Base page template' ),
]

WSGI_APPLICATION = 'app0.wsgi.application'

DEBUG = True
ALLOWED_HOSTS = [ "127.0.0.1", "*" ]
X_FRAME_OPTIONS = "SAMEORIGIN"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'ContainerAdministrator',
        'HOST': 'db',
        'PORT': 5432
    }
}

LANGUAGE_CODE = 'en'
LANGUAGES = [ ( 'en', 'English' ), ( 'ja', 'Japanese' ) ]

LOCALE_PATHS = [ BASE_DIR + "/locale" ]

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = "C:\\Static\\"
STATIC_URL = '/static/'

MEDIA_ROOT  = "C:\\Media\\"
MEDIA_URL = "/media/"

SESSION_REDIS = { "host": "redis", "db": 2, "prefix": "windev", "socket_timeout": 1 }
