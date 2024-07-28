from django.urls import (
    path,
    include
)

urlpatterns = [
    path('auth/', include('djoser.urls'), name="djoser"),
    path('auth/', include('djoser.urls.authtoken'), name="djoser_authtoken"),
    path('auth/', include('djoser.urls.jwt'), name="jwt"),
]