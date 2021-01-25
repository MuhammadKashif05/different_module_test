from django.conf.urls import url
from .pyzk import *
from .Pyzk_working import *
from .check_audit_flow import *

urlpatterns = [
    # url(r'^machine$', machine, name='machine'),
    url(r'^machine123$', machine123, name='machine123'),
    url(r'^create_user$', create_user123, name='create_user'),
    url(r'^create_client$', create_client, name='create_client'),
    url(r'^check_reversion$', check_reversion, name='check_reversion'),
    url(r'^update_client$', update_client, name='update_client'),
]
