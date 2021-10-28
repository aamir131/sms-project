from pathlib import Path,os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '=6ht-sekdv0+8z%+8a$_m)e4v$wnw=gel(7&qo!-rqa0p38vpi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MEDIA_URL="/media/"
MEDIA_ROOT= BASE_DIR/'media'

STATIC_URL="/static/"
STATIC_ROOT=BASE_DIR/'static'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'smsapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'smsapp.LoginCheckMiddleWare.LoginCheckMiddleWare',
]

ROOT_URLCONF = 'sms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['smsapp/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sms.wsgi.application'



DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE':'django.db.backends.mysql',
        'NAME':'student_management_system',
        'USER':'sms',
        'PASSWORD':'sms131',
        'HOST':'localhost',
        'PORT':'3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
AUTH_USER_MODEL="smsapp.CustomUser"
AUTHENTICATION_BACKENDS=['smsapp.EmailBackEnd.EmailBackEnd']

EMAIL_BACKEND="django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH=os.path.join(BASE_DIR,"sent_mails")

#EAMIL_HOST="smtp.gmail.com"
#EMAIL_PORT=7000
#EMAIL_HOST_USER="aamir13111"
#MAIL_HOST_PASSWORD="A@mir1311"
#EMAIL_USE_TLS=True
#DEFAULT_FROM_EMAIL="Student Management System <aamirkhan13111@gmail.com>"