
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from calculator_api.views import CalculatorAPIView, calculator_view


urlpatterns = [
    path('calculator/', CalculatorAPIView.as_view(), name='calculator'),
    path('', calculator_view, name='calculator_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
