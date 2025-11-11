from django.contrib import admin
from .models import User, Adm

admin.site.register(User)

@admin.register(Adm)
class AdmAdmin(admin.ModelAdmin):
    list_display = ('id_administracao', 'nome', 'email','senha', 'data_nascimento')
