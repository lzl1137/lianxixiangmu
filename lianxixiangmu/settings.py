

import os

#项目根目录
import sys

#os.path.dirname   获取文件的目录
#os.path.abspath   查看当前的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

#加密秘钥
SECRET_KEY = 'mk-wguemc*7vg6%s@y(d#!1=nvxr3g+we!qr^#8_rximn&5*$d'

#开发模式(上线设置为False)
DEBUG = True

#允许访问的ip地址(上线需要配置)
ALLOWED_HOSTS = []

#注册app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.account',
    'apps.cate',
    'apps.detail',
    'apps.main',
    'apps.search',
]

#中间注册
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#跟路由配置 一般不需要修改
ROOT_URLCONF = 'lianxixiangmu.urls'

#模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
#启动应用程序配置(一般不需要修改)
WSGI_APPLICATION = 'lianxixiangmu.wsgi.application'



#数据配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}



#用户密码验证配置(一般不需要修改)

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



#后台语言配置(开发中设置成中文)
LANGUAGE_CODE = 'zh-hans'
#时区设置
TIME_ZONE = 'UTC'
#国际化配置,自动转化多个语言
USE_I18N = True

USE_L10N = True
#开启django时区 如果不需要django时区可以设置成False(建议设置成False)
USE_TZ = True

#访问静态文件的路径配置
STATIC_URL = '/static/'
#配置静态文件 整理的根目录
STATIC_ROOT = 'static_root'
#静态文件目录配置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

#配置访问多媒体的路劲
MEDIA_URL = '/media/'
#配置文件上传的目录
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

