from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)

# Configuração do banco de dados Supabase
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('SUPABASE_DB', 'postgres'),
        'USER': os.getenv('SUPABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('SUPABASE_PASSWORD'),
        'HOST': os.getenv('SUPABASE_HOST'),
        'PORT': os.getenv('SUPABASE_PORT', '5432'),
        'OPTIONS': {
            'sslmode': 'require',  # Supabase exige SSL
        },
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('SUPABASE_PASSWORD'), 
        'HOST': 'db.zrnaighhtwddnibngduv.supabase.co',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',  # Supabase exige SSL
        },
    }
}

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configuração básica de cache (por arquivo)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'cache',
        'TIMEOUT': 60 * 15,  # 15 minutos
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

# Configurações da API REST
REST_FRAMEWORK = {
    # Padrão de paginação: 10 itens por página
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    # Permissões padrão (mude para IsAuthenticated quando implementar login)
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Cache e otimização
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
