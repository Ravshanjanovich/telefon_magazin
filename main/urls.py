from django.urls import path
from main.views import index, ContactFormView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index.as_view(), name='index'),
    path('', ContactFormView.as_view(), name='contact'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  