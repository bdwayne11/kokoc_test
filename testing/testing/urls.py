from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from testing import settings

urlpatterns = [
    path('', include('survey.urls', namespace='survey')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
