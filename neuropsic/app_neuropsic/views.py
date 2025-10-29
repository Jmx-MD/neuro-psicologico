from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Adm
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import json
import SUPABASE_URL, SUPABASE_KEY


load_dotenv() #variaveis de ambiente
supabase_url = os.getenv(SUPABASE_URL)
supabase_key = os.getenv(SUPABASE_KEY)
supabase: Client = create_client(supabase_url, supabase_key)

def home(request):
    return render(request, 'usuarios/home.html')

def novousuario(request):
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
    novo_user.est_civil = request.POST.get('est_civil')
    novo_user.escolaridade = request.POST.get('escolaridade')
    novo_user.st_moradia = request.POST.get('st_moradia')
    novo_user.residencia = request.POST.get('residencia')
    novo_user.st_ocupacional = request.POST.get('st_ocupacional')
    novo_user.fonte_renda= request.POST.get('fonte_renda')
    novo_user.pl_saude= request.POST.get('pl_saude')
    novo_user.cond_saude = request.POST.get('cond_saude')
    novo_user.hist_doencas = request.POST.get('hist_doencas')
    novo_user.int_hosp = request.POST.get('int_hosp')
    novo_user.dif_uri_evc= request.POST.get('dif_uri_evc')
    novo_user.hist_incont = request.POST.get('hist_incont')
    novo_user.uso_medic = request.POST.get('uso_medic')
    novo_user.tom_medic = request.POST.get('tom_medic')
    novo_user.ult_rev_medic = request.POST.get('ult_rev_medic')
    novo_user.desprec_medic = request.POST.get('desprec_medic')
    novo_user.seg_trat = request.POST.get('seg_trat')
    novo_user.apetite = request.POST.get('apetite')
    novo_user.cons_liq = request.POST.get('cons_liq')
    novo_user.cons_fibra = request.POST.get('cons_fibra')
    novo_user.alim_nutri = request.POST.get('alim_nutri')
    novo_user.adapt_queda = request.POST.get('adapt_queda')
    novo_user.sente_seg = request.POST.get('sente_seg')
    novo_user.disp_apoio = request.POST.get('disp_apoio')
    novo_user.n_quedas = request.POST.get('n_quedas')
    novo_user.les_quedas = request.POST.get('les_quedas')
    novo_user.hist_tabg = request.POST.get('hist_tabg')
    novo_user.hist_alc = request.POST.get('hist_alc')
    novo_user.ativ_fis = request.POST.get('ativ_fis')
    novo_user.saude_bucal= request.POST.get('saude_bucal')
    novo_user.cons_odont = request.POST.get('cons_odont')
    novo_user.dif_aud = request.POST.get('dif_aud')
    novo_user.st_visao = request.POST.get('st_visao')
    novo_user.vacinas = request.POST.get('vacinas')
    novo_user.atv_autocuid = request.POST.get('atv_autocuid')
    novo_user.atv_domes = request.POST.get('atv_domes')
    novo_user.atv_soc_lazer = request.POST.get('atv_soc_lazer')
    novo_user.mobilidade = request.POST.get('mobilidade')
    novo_user.func_cognitiv = request.POST.get('func_cognitiv')
    novo_user.atv_soc_ent = request.POST.get('atv_soc_ent')
    novo_user.atv_cult = request.POST.get('atv_cult')
    novo_user.atv_fis_rec = request.POST.get('atv_fis_rec')
    novo_user.atv_fam = request.POST.get('atv_fam')
    novo_user.atv_volunt = request.POST.get('atv_volunt')
    
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