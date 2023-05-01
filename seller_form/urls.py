
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from seller_survey.views import survey, submit_answer, results, clear_session



urlpatterns = [
    path('', survey, name='survey'),
    path('submit-answer/', submit_answer, name='submit_answer'),
    path('results/', results, name='results'),
    path('clear_session/', clear_session, name='clear_session'),
    path('admin/', admin.site.urls),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
