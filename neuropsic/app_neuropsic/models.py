from django.db import models
from datetime import date
from multiselectfield import MultiSelectField

class User(models.Model):
    # dados fixos
    id_user = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    
    
    #atualizaveis
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    
    
    #extra_data = models.JSONField(default=dict, blank=True)
    
    #inidicadores
    # === ETAPA 1: IDENTIFICAÇÃO ===
    idade = models.PositiveIntegerField(
        verbose_name="Idade (anos)",
        null=False
    )
    sexo = models.CharField(
        max_length=20,
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')],
        verbose_name="Sexo/Gênero"
    )

    # === DADOS SOCIODEMOGRÁFICOS (ordem exata da sua lista) ===
    est_civil = models.CharField(
        max_length=50,
        choices=[
            ('Solteiro(a)', 'Solteiro(a)'),
            ('Casado(a)/ União estável', 'Casado(a)/ União estável'),
            ('Viúvo(a)', 'Viúvo(a)'),
            ('Divorciado(a)/ Separado(a)', 'Divorciado(a)/ Separado(a)'),
        ],
        null=False,
        verbose_name="Estado Civil"
    )

    escolaridade = models.CharField(
        max_length=70,
        choices=[
            ('Nenhuma escolaridade formal', 'Nenhuma escolaridade formal'),
            ('Ensino Fundamental Incompleto', 'Ensino Fundamental Incompleto'),
            ('Ensino Fundamental Completo', 'Ensino Fundamental Completo'),
            ('Ensino Médio Incompleto', 'Ensino Médio Incompleto'),
            ('Ensino Médio Completo', 'Ensino Médio Completo'),
            ('Ensino Superior Incompleto', 'Ensino Superior Incompleto'),
            ('Ensino Superior Completo', 'Ensino Superior Completo'),
            ('Pós-graduação/ Mestrado/ Doutorado', 'Pós-graduação/ Mestrado/ Doutorado'),
        ],
        null=False,
        verbose_name="Escolaridade"
    )

    st_moradia = models.CharField(
        max_length=80,
        choices=[
            ('Mora sozinho(a)', 'Mora sozinho(a)'),
            ('Mora com conjugue/ parceiro(a)', 'Mora com conjugue/ parceiro(a)'),
            ('Mora com filhos', 'Mora com filhos'),
            ('Outro arranjo', 'Outro arranjo'),
            ('Mora em instituição (asilo, casa de repouso,ILPI)', 'Mora em instituição (asilo, casa de repouso,ILPI)'),
        ],
        null=False,
        verbose_name="Situação de Moradia"
    )

    residencia = models.CharField(
        max_length=60,
        choices=[
            ('Zona urbana', 'Zona urbana'),
            ('Zona rural', 'Zona rural'),
            ('Zona periurbana (transição entre zona urbana e rural)', 'Zona periurbana (transição entre zona urbana e rural)'),
        ],
        null=False,
        verbose_name="Área de Residência"
    )

    st_ocupacional = models.CharField(
        max_length=50,
        choices=[
            ('Aposentado(a)', 'Aposentado(a)'),
            ('Trabalha atualmente', 'Trabalha atualmente'),
            ('Desempregado(a)', 'Desempregado(a)'),
            ('Do lar', 'Do lar'),
            ('Outro', 'Outro'),
        ],
        null=False,
        verbose_name="Situação Ocupacional"
    )

    fonte_renda = models.CharField(
        max_length=60,
        choices=[
            ('Aposentadoria/Pensão', 'Aposentadoria/Pensão'),
            ('Salário', 'Salário'),
            ('Benefício social (BPC, Bolsa Família, etc.)', 'Benefício social (BPC, Bolsa Família, etc.)'),
            ('Auxílio de familiares', 'Auxílio de familiares'),
            ('Não possui renda', 'Não possui renda'),
        ],
        null=False,
        verbose_name="Fonte de Renda"
    )

    pl_saude = models.CharField(
        max_length=30,
        choices=[
            ('SUS', 'SUS'),
            ('Plano privado', 'Plano privado'),
            ('Particular', 'Particular'),
            ('Não possui', 'Não possui'),
        ],
        null=False,
        verbose_name="Plano de Saúde"
    )

    cond_saude = models.CharField(
        max_length=20,
        choices=[
            ('Ótima', 'Ótima'),
            ('Boa', 'Boa'),
            ('Regular', 'Regular'),
            ('Ruim', 'Ruim'),
            ('Muito ruim', 'Muito ruim'),
        ],
        null=False,
        verbose_name="Condição de Saúde Autopercebida"
    )

    # === HISTÓRICO MÉDICO ===
    hist_doencas = MultiSelectField(
        choices=[
            ('Hipertensão arterial', 'Hipertensão arterial'),
            ('Diabetes', 'Diabetes'),
            ('Doença cardíaca', 'Doença cardíaca'),
            ('Doença pulmonar (DPOC, asma)', 'Doença pulmonar (DPOC, asma)'),
            ('Câncer', 'Câncer'),
            ('Doença renal', 'Doença renal'),
            ('Artrite/ Artrose', 'Artrite/ Artrose'),
            ('Depressão', 'Depressão'),
            ('Ansiedade', 'Ansiedade'),
            ('Outra doença crônica', 'Outra doença crônica'),
            ('Nenhuma', 'Nenhuma'),
        ],
        null=False,
        verbose_name="Histórico de Doenças"
    )

    # === ETAPA 2: HISTÓRICO MÉDICO E COMPORTAMENTAL ===

    # Internações
    int_hosp = models.CharField(
        max_length=50,
        choices=[
            ('Sim, uma vez', 'Sim, uma vez'),
            ('Sim, duas ou mais vezes', 'Sim, duas ou mais vezes'),
            ('Não', 'Não'),
        ],
        verbose_name="Internações hospitalares (último ano)",
        null=False
    )

    # Dificuldade urinária/evacuação
    dif_uri_evc = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Ocasionalmente', 'Ocasionalmente'),
            ('Não', 'Não'),
        ],
        verbose_name="Tem dificuldades para urinar ou evacuar?",
        null=False
    )

    # Incontinência
    hist_incont = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Ocasionalmente', 'Ocasionalmente'),
            ('Não', 'Não'),
        ],
        verbose_name="Há episódios de incontinência urinária ou fecal?",
        null=False
    )

    # Uso de medicamentos
    uso_medic = models.CharField(
        max_length=50,
        choices=[
            ('Não usa medicamentos', 'Não usa medicamentos'),
            ('Sim, 1 a 2 medicamentos', 'Sim, 1 a 2 medicamentos'),
            ('Sim, 3 a 4 medicamentos', 'Sim, 3 a 4 medicamentos'),
            ('Sim, 5 ou mais medicamentos', 'Sim, 5 ou mais medicamentos'),
        ],
        verbose_name="Uso de medicamentos de forma contínua",
        null=False
    )

    # Toma corretamente
    seg_trat = models.CharField(
        max_length=50,
        choices=[
            ('Sim, conforme prescrito', 'Sim, conforme prescrito'),
            ('Às vezes esqueço', 'Às vezes esqueço'),
            ('Raramente sigo as orientações', 'Raramente sigo as orientações'),
        ],
        verbose_name="Está tomando todos os medicamentos prescritos corretamente?",
        null=False
    )

    # Última revisão de medicamentos
    ult_rev_medic = models.CharField(
        max_length=50,
        choices=[
            ('Menos de 6 meses', 'Menos de 6 meses'),
            ('Entre 6 meses e 1 ano', 'Entre 6 meses e 1 ano'),
            ('Mais de 1 ano', 'Mais de 1 ano'),
            ('Não sei', 'Não sei'),
        ],
        verbose_name="Quando foi a última revisão dos medicamentos pelo médico?",
        null=False
    )

    # Desprescrição
    desprec_medic = models.CharField(
        max_length=50,
        choices=[
            ('Menos de 6 meses', 'Menos de 6 meses'),
            ('Entre 6 meses e 1 ano', 'Entre 6 meses e 1 ano'),
            ('Mais de 1 ano', 'Mais de 1 ano'),
            ('Não sei', 'Não sei'),
        ],
        verbose_name="Já houve desprescrição de algum medicamento?",
        null=False
    )

    # Segue tratamento
    tom_medic = models.CharField(
        max_length=50,
        choices=[
            ('Sempre', 'Sempre'),
            ('Na maioria das vezes', 'Na maioria das vezes'),
            ('Raramente', 'Raramente'),
            ('Nunca', 'Nunca'),
        ],
        verbose_name="Está seguindo o tratamento recomendado?",
        null=False
    )

    # === NUTRIÇÃO ===
    apetite = models.CharField(
        max_length=50,
        choices=[
            ('Normal como de costume', 'Normal como de costume'),
            ('Diminuiu no último ano', 'Diminuiu no último ano'),
            ('Aumentou no último ano', 'Aumentou no último ano'),
        ],
        verbose_name="Como está o apetite?",
        null=False
    )

    cons_liq = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Às vezes', 'Às vezes'),
            ('Não', 'Não'),
        ],
        verbose_name="Consome líquidos suficientes?",
        null=False
    )

    cons_fibra = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Parcialmente', 'Parcialmente'),
            ('Não', 'Não'),
        ],
        verbose_name="Consome fibras e líquidos adequadamente?",
        null=False
    )

    alim_nutri = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Parcialmente', 'Parcialmente'),
            ('Não', 'Não'),
        ],
        verbose_name="A alimentação é variada e rica em nutrientes?",
        null=False
    )

    # === QUEDAS ===
    adapt_queda = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Parcialmente', 'Parcialmente'),
            ('Não', 'Não'),
        ],
        verbose_name="O ambiente está adaptado para evitar quedas?",
        null=False
    )

    sente_seg = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Não', 'Não'),
            ('Não sei', 'Não sei'),
        ],
        verbose_name="Se sente segura na própria casa?",
        null=False
    )

    disp_apoio = models.CharField(
        max_length=50,
        choices=[
            ('Sim', 'Sim'),
            ('Não, mas deveria usar', 'Não, mas deveria usar'),
            ('Não', 'Não'),
        ],
        verbose_name="Utiliza dispositivos de apoio?",
        null=False
    )

    n_quedas = models.PositiveIntegerField(
        verbose_name="Quedas (últimos 12 meses) - Quantas?",
        null=False,
        default=0
    )

    les_quedas = models.CharField(
        max_length=100,
        choices=[
            ('Sim, nenhuma lesão', 'Sim, nenhuma lesão'),
            ('Sim, com lesão leve (ex.: escoriações)', 'Sim, com lesão leve (ex.: escoriações)'),
            ('Sim, com fratura ou lesão grave', 'Sim, com fratura ou lesão grave'),
            ('Não', 'Não'),
        ],
        verbose_name="Quedas - Lesão",
        null=False
    )

    # === COMPORTAMENTOS DE RISCO ===
    hist_tabg = models.CharField(
        max_length=60,
        choices=[
            ('Nunca fumou', 'Nunca fumou'),
            ('Ex-fumante (parou há mais de 10 anos)', 'Ex-fumante (parou há mais de 10 anos)'),
            ('Ex-fumante (parou há menos de 5 anos)', 'Ex-fumante (parou há menos de 5 anos)'),
            ('Fuma ocasionalmente', 'Fuma ocasionalmente'),
            ('Fuma diariamente', 'Fuma diariamente'),
        ],
        verbose_name="Histórico de tabagismo",
        null=False
    )

    hist_alc = models.CharField(
        max_length=60,
        choices=[
            ('Nunca', 'Nunca'),
            ('1 vez por mês', '1 vez por mês'),
            ('1 a 3 vezes por mês', '1 a 3 vezes por mês'),
            ('1 a 3 vezes por semana', '1 a 3 vezes por semana'),
            ('4 ou mais vezes por semana', '4 ou mais vezes por semana'),
        ],
        verbose_name="Histórico de consumo de álcool",
        null=False
    )

    ativ_fis = models.CharField(
        max_length=60,
        choices=[
            ('Nunca', 'Nunca'),
            ('1 vez por semana ou menos', '1 vez por semana ou menos'),
            ('2 a 3 vezes por semana', '2 a 3 vezes por semana'),
            ('4 a 5 vezes por semana', '4 a 5 vezes por semana'),
            ('Todos os dias', 'Todos os dias'),
        ],
        verbose_name="Atividade física (últimos 3 meses)",
        null=False
    )

    # === SAÚDE BUCAL E SENSORIAL ===
    saude_bucal = models.CharField(
        max_length=50,
        choices=[
            ('Adequada (sem queixas)', 'Adequada (sem queixas)'),
            ('Algum desconforto ou dor', 'Algum desconforto ou dor'),
            ('Problemas', 'Problemas'),
        ],
        verbose_name="Como está a saúde bucal?",
        null=False
    )

    cons_odont = models.CharField(
        max_length=50,
        choices=[
            ('Não', 'Não'),
            ('Sim, 1 vez', 'Sim, 1 vez'),
            ('Sim, 2 vezes ou mais', 'Sim, 2 vezes ou mais'),
        ],
        verbose_name="Saúde bucal (consultas odontológicas, últimos 12 meses)",
        null=False
    )

    dif_aud = models.CharField(
        max_length=60,
        choices=[
            ('Sim, uso aparelho auditivo', 'Sim, uso aparelho auditivo'),
            ('Sim, não uso aparelho', 'Sim, não uso aparelho'),
            ('Não', 'Não'),
        ],
        verbose_name="Há dificuldades auditivas?",
        null=False
    )

    st_visao = models.CharField(
        max_length=60,
        choices=[
            ('Não', 'Não'),
            ('Interfere parcialmente', 'Interfere parcialmente'),
            ('Interfere muito', 'Interfere muito'),
        ],
        verbose_name="A visão interfere nas atividades diárias?",
        null=False
    )

    # === VACINAS (MultiSelectField) ===
    vacinas = MultiSelectField(
        choices=[
            ('Gripe (influenza)', 'Gripe (influenza)'),
            ('Pneumocócica', 'Pneumocócica'),
            ('COVID-19 (reforço)', 'COVID-19 (reforço)'),
        ],
        verbose_name="Vacinação (últimos 12 meses)",
        null=False,
        blank=True
    )

    # === ATIVIDADES FUNCIONAIS (arrays no Supabase → MultiSelectField) ===
    atv_autocuid = MultiSelectField(
        choices=[
            ('Alimenta-se sozinho(a)', 'Alimenta-se sozinho(a)'),
            ('Toma banho ou higiene pessoal', 'Toma banho ou higiene pessoal'),
            ('Vai ao banheiro sozinho(a)', 'Vai ao banheiro sozinho(a)'),
            ('Deita-se/levanta-se da cama ou cadeira', 'Deita-se/levanta-se da cama ou cadeira'),
            ('Nenhuma dificuldade observada', 'Nenhuma dificuldade observada'),
        ],
        null=False,
        verbose_name="Atividades de Autocuidado"
    )

    atv_domes = MultiSelectField(
        choices=[
            ('Prepara refeições', 'Prepara refeições'),
            ('Faz compras de alimentos ou itens de casa', 'Faz compras de alimentos ou itens de casa'),
            ('Lava roupas ou limpar a casa', 'Lava roupas ou limpar a casa'),
            ('Controla as próprias finanças/pagar contas', 'Controla as próprias finanças/pagar contas'),
            ('Usa telefone ou celular', 'Usa telefone ou celular'),
            ('Nenhuma dificuldade observada', 'Nenhuma dificuldade observada'),
        ],
        null=False,
        verbose_name="Atividades Domésticas"
    )

    atv_soc_lazer = MultiSelectField(
        choices=[
            ('Participa de atividades religiosas, culturais ou sociais', 'Participa de atividades religiosas, culturais ou sociais'),
            ('Mantem hobbies ou passatempos (ex.: jardinagem, música, leitura)', 'Mantem hobbies ou passatempos (ex.: jardinagem, música, leitura)'),
            ('Sai de casa para lazer (ex.: visitas, cinema, encontros)', 'Sai de casa para lazer (ex.: visitas, cinema, encontros)'),
            ('Conversa/interage com amigos ou familiares', 'Conversa/interage com amigos ou familiares'),
            ('Nenhuma dificuldade observada', 'Nenhuma dificuldade observada'),
        ],
        null=False,
        verbose_name="Atividades Sociais e Lazer"
    )

    mobilidade = MultiSelectField(
        choices=[
            ('Caminha dentro de casa', 'Caminha dentro de casa'),
            ('Caminha longas distâncias (mais de 400m)', 'Caminha longas distâncias (mais de 400m)'),
            ('Sobe ou desce escadas', 'Sobe ou desce escadas'),
            ('Nenhuma dificuldade observada', 'Nenhuma dificuldade observada'),
        ],
        null=False,
        verbose_name="Mobilidade"
    )

    func_cognitiv = MultiSelectField(
        choices=[
            ('Lembra compromissos ou conversas recentes', 'Lembra compromissos ou conversas recentes'),
            ('Encontra objetos pessoais', 'Encontra objetos pessoais'),
            ('Reconhece pessoas próximas', 'Reconhece pessoas próximas'),
            ('Segue instruções simples', 'Segue instruções simples'),
            ('Nenhuma dificuldade observada', 'Nenhuma dificuldade observada'),
        ],
        null=False,
        verbose_name="Função Cognitiva"
    )

    atv_soc_ent = MultiSelectField(
        choices=[
            ('Conversar com amigos ou familiares', 'Conversar com amigos ou familiares'),
            ('Participar de grupos comunitários, associações ou clubes', 'Participar de grupos comunitários, associações ou clubes'),
            ('Participar de eventos sociais (festas, encontros, reuniões)', 'Participar de eventos sociais (festas, encontros, reuniões)'),
            ('Nenhuma dessas', 'Nenhuma dessas'),
        ],
        null=False,
        verbose_name="Atividades Sociais de Entretenimento"
    )

    atv_cult = MultiSelectField(
        choices=[
            ('Ler livros, jornais ou revistas', 'Ler livros, jornais ou revistas'),
            ('Assistir televisão, ouvir rádio, ouvir música', 'Assistir televisão, ouvir rádio, ouvir música'),
            ('Ir ao cinema, teatro ou shows', 'Ir ao cinema, teatro ou shows'),
            ('Nenhuma dessas', 'Nenhuma dessas'),
        ],
        null=False,
        verbose_name="Atividades Culturais"
    )

    atv_fis_rec = MultiSelectField(
        choices=[
            ('Caminhadas ou passeios ao ar livre', 'Caminhadas ou passeios ao ar livre'),
            ('Jardinagem ou cuidar de plantas', 'Jardinagem ou cuidar de plantas'),
            ('Dança ou ginástica leve', 'Dança ou ginástica leve'),
            ('Nenhuma dessas', 'Nenhuma dessas'),
        ],
        null=False,
        verbose_name="Atividades Físicas Recreativas"
    )

    atv_fam = MultiSelectField(
        choices=[
            ('Passar tempo com netos ou bisnetos', 'Passar tempo com netos ou bisnetos'),
            ('Cuidar de familiares', 'Cuidar de familiares'),
            ('Preparar refeições e compartilhar momentos em família', 'Preparar refeições e compartilhar momentos em família'),
            ('Reunir a família em datas especiais', 'Reunir a família em datas especiais'),
            ('Nenhuma dessas', 'Nenhuma dessas'),
        ],
        null=False,
        verbose_name="Atividades Familiares"
    )

    atv_volunt = MultiSelectField(
        choices=[
            ('Ajudar vizinhos ou amigos', 'Ajudar vizinhos ou amigos'),
            ('Fazer trabalho voluntário em instituições', 'Fazer trabalho voluntário em instituições'),
            ('Ensinar ou compartilhar conhecimentos com outras pessoas', 'Ensinar ou compartilhar conhecimentos com outras pessoas'),
            ('Nenhuma dessas', 'Nenhuma dessas'),
        ],
        null=False,
        verbose_name="Atividades Voluntárias"
    )

    def __str__(self):
        return f"Questionário ID {self.id}"

    class Meta:
        db_table = 'questionario'  # opcional: nome exato da tabela no Supabase
        verbose_name = "Questionário Completo"
        
    def __str__(self):
        return self.nome      

class Adm(models.Model):
    id_administracao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome

    

