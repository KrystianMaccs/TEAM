from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
]

admin.site.site_header = "TEAM: The Enlightened Atheist Movement"
admin.site.site_title = "TEAM: The Enlightened Atheist Movement Portal"
admin.site.index_title = "Welcome to the TEAM: The Enlightened Atheist Movement Portal"