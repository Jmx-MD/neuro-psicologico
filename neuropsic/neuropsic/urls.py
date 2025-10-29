from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_neuropsic.viewsets import UserViewSet, AdmViewSet
from django.http import JsonResponse # health check
from app_neuropsic import views

def health_check(request):
    return JsonResponse({"status": "ok"})

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'adms', AdmViewSet, basename='adm')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', health_check),
    path('api/criar-usuario/', views.criar_usuario, name='criar_usuario'),
]
