from rest_framework import viewsets, permissions
from .models import User, Adm
from .serializers import UserSerializer, AdmSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60*5), name='dispatch')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id_user')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # CHANGE to IsAuthenticated in production

class AdmViewSet(viewsets.ModelViewSet):
    queryset = Adm.objects.all().order_by('id_administracao')
    serializer_class = AdmSerializer
    permission_classes = [permissions.IsAuthenticated]
