from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'cnn_classification'

urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
