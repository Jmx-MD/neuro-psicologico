from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Adm
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import json
load_dotenv() #variaveis de ambiente


supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_ANON_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

def home(request):
    return render(request, 'usuarios/home.html')

def novousuario(request):
    breakpoint()
    #dados fixos
    novo_user = User()
    novo_user.nome = request.POST.get('nome')
    novo_user.sexo = request.POST.get('sexo')
    
    #atualizaveis
    novo_user.idade = request.POST.get('idade')
    novo_user.email = request.POST.get('email')
    novo_user.senha = request.POST.get('senha')
    
    #indicadores iniciais
    novo_user.idade = request.POST.get('idade')
    novo_user.estadosCivis = request.POST.get('estadosCivis')
    novo_user.escolaridade = request.POST.get('escolaridade')
    novo_user.moradias = request.POST.get('escolaridade')
    novo_user.residencias = request.POST.get('residencias')
    novo_user.ocupacoes = request.POST.get('ocupacoes')
    novo_user.rendaMensal = request.POST.get('rendaMensal')
    novo_user.fontesRenda= request.POST.get('fontesRenda')
    novo_user.planosSaude= request.POST.get('planosSaude')
    novo_user.condicoesSaude = request.POST.get('condicoesSaude')
    novo_user.doencasCronicas = request.POST.get('doencasCronicas')
    novo_user.outraDoencaCronica= request.POST.get('outraDoencaCronica')
    novo_user.internacoes = request.POST.get('internacoes')
    novo_user.dificuldadesUrinarias = request.POST.get('dificuldadesUrinarias')
    novo_user.incontinencia = request.POST.get('incontinencia')
    novo_user.usoMedicamentos = request.POST.get('usoMedicamentos')
    novo_user.tomandoMedicamentos = request.POST.get('tomandoMedicamentos')
    novo_user.revisaoMedicamentos = request.POST.get('revisaoMedicamentos')
    novo_user.desprescricaoMedicamentos = request.POST.get('desprescricaoMedicamentos')
    novo_user.seguindoTratamento = request.POST.get('seguindoTratamento')
    novo_user.apetite = request.POST.get('apetite')
    novo_user.consumoLiquidos = request.POST.get('consumoLiquidos')
    novo_user.consumoFibras = request.POST.get('consumoFibras')
    novo_user.alimentacaoVariada = request.POST.get('alimentacaoVariada')
    novo_user.ambienteAdaptado = request.POST.get('ambienteAdaptado')
    novo_user.seguraCasa = request.POST.get('seguraCasa')
    novo_user.dispositivosApoio = request.POST.get('dispositivosApoio')
    novo_user.nQuedas = request.POST.get('nQuedas')
    novo_user.quedasLesao = request.POST.get('quedasLesao')
    novo_user.tabagismo = request.POST.get('tabagismo')
    novo_user.alcool = request.POST.get('alcool')
    novo_user.atividadeFisica = request.POST.get('atividadeFisica')
    novo_user.saudeBucal= request.POST.get('saudeBucal')
    novo_user.consultasOdonto = request.POST.get('consultasOdonto')
    novo_user.dificuldadesAuditivas = request.POST.get('dificuldadesAuditivas')
    novo_user.visaoInterfere = request.POST.get('visaoInterfere')
    novo_user.vacinacao = request.POST.get('vacinacao')
    novo_user.autocuidado = request.POST.get('autocuidado')
    novo_user.atividadesDomesticas = request.POST.get('atividadesDomesticas')
    novo_user.atividadesSociaisLazer = request.POST.get('atividadesSociaisLazer')
    novo_user.mobilidade = request.POST.get('mobilidade')
    novo_user.funcoesCognitivas = request.POST.get('funcoesCognitivas')
    novo_user.atividadesSociais = request.POST.get('atividadesSociais')
    novo_user.atividadesLazer = request.POST.get('atividadesLazer')
    novo_user.atividadesCulturais = request.POST.get('atividadesCulturais')
    novo_user.atividadesFisicasRecreativas = request.POST.get('atividadesFisicasRecreativas')
    novo_user.atividadesFamiliares = request.POST.get('atividadesFamiliares')
    novo_user.atividadesVoluntariado = request.POST.get('atividadesVoluntariado')

    
    novo_user.save() #salva no db
    Usuarios = { 'novousuario': User.objects.all()}
    return render(request, 'usuarios/usuarios.html', {'user': novo_user})   

    
    

    


#func grok
@csrf_exempt  # Disable CSRF for simplicity (enable in production)
def submit_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')

            if not name or not email:
                return JsonResponse({'error': 'Name and email are required'}, status=400)

            # Insert into Supabase
            response = supabase.table('users').insert({'name': name, 'email': email}).execute()

            if hasattr(response, 'error') and response.error:
                return JsonResponse({'error': 'Failed to save data'}, status=500)

            return JsonResponse({'message': 'Data saved successfully', 'data': response.data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
