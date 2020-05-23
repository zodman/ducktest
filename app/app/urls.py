from django.urls import  path, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   path('admin/', admin.site.urls),
   path("admin/", include('loginas.urls')),
   path('accounts/', include('registration.backends.simple.urls')),
   path('', TemplateView.as_view(template_name='base.html'), name="index"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
