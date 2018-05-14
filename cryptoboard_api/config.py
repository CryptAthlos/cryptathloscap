def db():

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cryptos',
            'USER': 'crypto',
            'PASSWORD': '0lympu$24$jmfISU',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
    return DATABASES


def secret_key():

    SECRET_KEY = 'rykq2vljr$^lrezlf3#5+nf_m==$2g=f6=39=1azf2d!aiy4w*'
    return SECRET_KEY
