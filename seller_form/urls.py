
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from seller_survey.views import survey, submit_answer



urlpatterns = [
    path('', survey, name='survey'),
    path('submit-answer/', submit_answer, name='submit_answer'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
