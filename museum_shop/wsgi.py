"""
WSGI config for museum_shop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent.parent

from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(BASE_DIR, 'src'))
sys.path.append(os.path.join(BASE_DIR, 'src', 'museum_shop'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'museum_shop.settings')

application = get_wsgi_application()
