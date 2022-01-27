
import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nft.settings')
app = Celery('nft')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Europe/London'
 
app.autodiscover_tasks()
 
 
