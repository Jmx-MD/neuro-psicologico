from django.contrib import admin
from .models import User, Adm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'nome', 'email','senha', 'data_nascimento')

@admin.register(Adm)
class AdmAdmin(admin.ModelAdmin):
    list_display = ('id_administracao', 'nome', 'email','senha', 'data_nascimento')
