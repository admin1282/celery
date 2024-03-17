from core.views import task, check_result
from django.urls import path

urlpatterns = [
    path('snippets', task),
    path('snippets_session', check_result)
]