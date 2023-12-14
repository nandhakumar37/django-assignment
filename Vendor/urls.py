from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('vendor/',include('vendor_app.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
