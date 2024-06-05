from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogViewSet, AlertViewSet, log_upload, detect_anomaly
from django.contrib import admin
from siem_app.views import root_view
 
router = DefaultRouter()
router.register(r'logs', LogViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('/', include('siem_app.urls')),
    path('api/log_upload/', log_upload),
    path('api/detect-anomaly/', detect_anomaly),
    path('admin/', admin.site.urls),
    path('', root_view),
]

from django.urls import path
from .views import log_upload, detect_anomaly


