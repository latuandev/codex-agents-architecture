from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health_check(request):
    """
    Return a minimal process health response.
    """
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
]
