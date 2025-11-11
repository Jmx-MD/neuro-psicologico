from django.db import models
from datetime import date

class User(models.Model):
    id_user = models.AutoField(primary_key=True)

    # === ETAPA 1: IDENTIFICAÇÃO ===
    idade = models.PositiveIntegerField(verbose_name="Idade (anos)", null=False)

    sexo = models.CharField(
        max_length=20,
        choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')],
        verbose_name="Sexo/Gênero"
    )

    estadosCivis = models.CharField(
        max_length=50,
        choices=[
            ('Solteiro(a)', 'Solteiro(a)'),
            ('Casado(a)/ União estável', 'Casado(a)/ União estável'),
            ('Viúvo(a)', 'Viúvo(a)'),
            ('Divorciado(a)/ Separado(a)', 'Divorciado(a)/ Separado(a)'),
        ],
        verbose_name="Estado Civil"
    )

    escolaridade = models.CharField(
        max_length=70,
        choices=[
            ('Nenhuma escolaridade formal', 'Nenhuma escolaridade formal'),
            ('Ensino fundamental incompleto', 'Ensino fundamental incompleto'),
            ('Ensino fundamental completo', 'Ensino Fundamental completo'),
            ('Ensino médio incompleto', 'Ensino médio incompleto'),
            ('Ensino médio completo', 'Ensino médio completo'),
            ('Ensino superior incompleto', 'Ensino superior incompleto'),
            ('Ensino superior completo', 'Ensino superior completo'),
            ('Pós-graduação', 'Pós-graduação'),
        ],
        verbose_name="Escolaridade"
    )

    moradias = models.CharField(
        max_length=80,
        choices=[
            ('Mora sozinho(a)', 'Mora sozinho(a)'),
            ('Mora com cônjuge/companheiro(a)', 'Mora com cônjugue/companheiro(a)'),
            ('Mora com filhos', 'Mora com filhos'),
            ('Outro arranjo', 'Outro arranjo'),
            ('Mora em instituição (asilo, casa de repouso, ILPI)', 'Mora em instituição (asilo, casa de repouso, ILPI)'),
        ],
        verbose_name="Situação de Moradia"
    )

    residencias = models.CharField(
        max_length=60,
        choices=[
            ('Zona urbana', 'Zona urbana'),
            ('Zona rural', 'Zona rural'),
            ('Zona periurbana (transição)', 'Zona periurbana (transição)'),
        ],
        verbose_name="Área de Residência"
    )

    ocupacoes = models.CharField(
        max_length=50,
        choices=[
            ('Aposentado(a)', 'Aposentado(a)'),
            ('Trabalhador(a) ativo(a)', 'Trabalhador(a) ativo(a)'),
            ('Desempregado(a)', 'Desempregado(a)'),
            ('Trabalho voluntário', 'Trabalho voluntário'),
            ('Outro', 'Outro'),
        ],
        verbose_name="Situação Ocupacional"
    )

    rendaMensal = models.IntegerField(verbose_name='Renda Mensal (em salários mínimos)')

    fontesRenda = models.CharField(
        max_length=255,
        choices=[
            ('Aposentadoria/pensão', 'Aposentadoria/pensão'),
            ('Trabalho remunerado', 'Trabalho remunerado'),
            ('Apoio familiar', 'Apoio familiar'),
            ('Benefícios sociais (ex.: Programas governamentais como Bolsa Família ou equivalente)', 'Benefícios sociais (ex.: Programas governamentais como Bolsa Família ou equivalente)'),
            ('Outro', 'Outro'),
        ],
        verbose_name="Fonte de Renda"
    )

    planosSaude = models.CharField(
        max_length=255,
        choices=[
            ('Apenas sistema público (SUS)', 'Apenas sistema público (SUS)'),
            ('Apenas plano privado', 'Apenas plano privado'),
            ('Sistema público + plano privado', 'Sistema público + plano privado'),
            ('Nenhum', 'Nenhum'),
        ],
        verbose_name="Plano de Saúde"
    )

    condicoesSaude = models.CharField(
        max_length=20,
        choices=[
            ('Muito boa', 'Muito boa'),
            ('Boa', 'Boa'),
            ('Regular', 'Regular'),
            ('Ruim', 'Ruim'),
            ('Muito ruim', 'Muito ruim'),
        ],
        verbose_name="Condição de Saúde Autopercebida"
    )

    DIFICULDADES_URINARIAS_CHOICES = [
        ('Sim', 'Sim'),
        ('Ocasionalmente', 'Ocasionalmente'),
        ('Não', 'Não'),
    ]

    INCONTINENCIA_CHOICES = DIFICULDADES_URINARIAS_CHOICES

    USO_MEDICAMENTOS_CHOICES = [
        ('Não usa medicamentos', 'Não usa medicamentos'),
        ('Sim, 1 a 2 medicamentos', 'Sim, 1 a 2 medicamentos'),
        ('Sim, 3 a 4 medicamentos', 'Sim, 3 a 4 medicamentos'),
        ('Sim, 5 ou mais medicamentos', 'Sim, 5 ou mais medicamentos'),
    ]

    TOMANDO_MEDICAMENTOS_CHOICES = [
        ('Sim, conforme prescrito', 'Sim, conforme prescrito'),
        ('Às vezes esqueço', 'Às vezes esqueço'),
        ('Raramente sigo as orientações', 'Raramente sigo as orientações'),
    ]

    REVISAO_MEDICAMENTOS_CHOICES = [
        ('Menos de 6 meses', 'Menos de 6 meses'),
        ('Entre 6 meses e 1 ano', 'Entre 6 meses e 1 ano'),
        ('Mais de 1 ano', 'Mais de 1 ano'),
        ('Não sei', 'Não sei'),
    ]

    DESPRESCRICAO_MEDICAMENTOS_CHOICES = REVISAO_MEDICAMENTOS_CHOICES

    SEGUINDO_TRATAMENTO_CHOICES = [
        ('Sempre', 'Sempre'),
        ('Na maioria das vezes', 'Na maioria das vezes'),
        ('Raramente', 'Raramente'),
        ('Nunca', 'Nunca'),
    ]

    APETITE_CHOICES = [
        ('Normal como de costume', 'Normal como de costume'),
        ('Diminuiu no último ano', 'Diminuiu no último ano'),
        ('Aumentou no último ano', 'Aumentou no último ano'),
    ]

    CONSUMO_LIQUIDOS_CHOICES = [
        ('Sim', 'Sim'),
        ('Às vezes', 'Às vezes'),
        ('Não', 'Não'),
    ]

    CONSUMO_FIBRAS_CHOICES = [
        ('Sim', 'Sim'),
        ('Parcialmente', 'Parcialmente'),
        ('Não', 'Não'),
    ]

    ALIMENTACAO_VARIADA_CHOICES = CONSUMO_FIBRAS_CHOICES
    AMBIENTE_ADAPTADO_CHOICES = CONSUMO_FIBRAS_CHOICES

    SEGURA_CASA_CHOICES = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Não sei', 'Não sei'),
    ]

    DISPOSITIVOS_APOIO_CHOICES = [
        ('Sim', 'Sim'),
        ('Não, mas deveria usar', 'Não, mas deveria usar'),
        ('Não', 'Não'),
    ]

    QUEDAS_LESOES_CHOICES = [
        ('Sim, nenhuma lesão', 'Sim, nenhuma lesão'),
        ('Sim, com lesão leve (ex.: escoriações)', 'Sim, com lesão leve (ex.: escoriações)'),
        ('Sim, com fratura ou lesão grave', 'Sim, com fratura ou lesão grave'),
        ('Não', 'Não'),
    ]

    TABAGISMO_CHOICES = [
        ('Nunca fumou', 'Nunca fumou'),
        ('Ex-fumante (parou há mais de 10 anos)', 'Ex-fumante (parou há mais de 10 anos)'),
        ('Ex-fumante (parou há menos de 5 anos)', 'Ex-fumante (parou há menos de 5 anos)'),
        ('Fuma ocasionalmente', 'Fuma ocasionalmente'),
        ('Fuma diariamente', 'Fuma diariamente'),
    ]

    ALCOOL_CHOICES = [
        ('Nunca', 'Nunca'),
        ('1 vez por mês', '1 vez por mês'),
        ('1 a 3 vezes por mês', '1 a 3 vezes por mês'),
        ('1 a 3 vezes por semana', '1 a 3 vezes por semana'),
        ('4 ou mais vezes por semana', '4 ou mais vezes por semana'),
    ]

    ATIVIDADE_FISICA_CHOICES = [
        ('Nunca', 'Nunca'),
        ('1 vez por semana ou menos', '1 vez por semana ou menos'),
        ('2 a 3 vezes por semana', '2 a 3 vezes por semana'),
        ('4 a 5 vezes por semana', '4 a 5 vezes por semana'),
        ('Todos os dias', 'Todos os dias'),
    ]

    SAUDE_BUCAL_CHOICES = [
        ('Adequada (sem queixas)', 'Adequada (sem queixas)'),
        ('Algum desconforto ou dor', 'Algum desconforto ou dor'),
        ('Problemas', 'Problemas'),
    ]

    CONSULTAS_ODONTO_CHOICES = [
        ('Não', 'Não'),
        ('Sim, 1 vez', 'Sim, 1 vez'),
        ('Sim, 2 vezes ou mais', 'Sim, 2 vezes ou mais'),
    ]

    DIFICULDADES_AUDITIVAS_CHOICES = [
        ('Sim, uso aparelho auditivo', 'Sim, uso aparelho auditivo'),
        ('Sim, não uso aparelho', 'Sim, não uso aparelho'),
        ('Não', 'Não'),
    ]

    VISAO_INTERFERE_CHOICES = [
        ('Não', 'Não'),
        ('Interfere parcialmente', 'Interfere parcialmente'),
        ('Interfere muito', 'Interfere muito'),
    ]

    # ========= CAMPOS =========

    dificuldadesUrinarias = models.CharField(max_length=50, choices=DIFICULDADES_URINARIAS_CHOICES)
    incontinencia = models.CharField(max_length=50, choices=INCONTINENCIA_CHOICES)
    usoMedicamentos = models.CharField(max_length=80, choices=USO_MEDICAMENTOS_CHOICES)
    tomandoMedicamentos = models.CharField(max_length=80, choices=TOMANDO_MEDICAMENTOS_CHOICES)
    revisaoMedicamentos = models.CharField(max_length=80, choices=REVISAO_MEDICAMENTOS_CHOICES)
    desprescricaoMedicamentos = models.CharField(max_length=80, choices=DESPRESCRICAO_MEDICAMENTOS_CHOICES)
    seguindoTratamento = models.CharField(max_length=80, choices=SEGUINDO_TRATAMENTO_CHOICES)
    apetite = models.CharField(max_length=80, choices=APETITE_CHOICES)
    consumoLiquidos = models.CharField(max_length=80, choices=CONSUMO_LIQUIDOS_CHOICES)
    consumoFibras = models.CharField(max_length=80, choices=CONSUMO_FIBRAS_CHOICES)
    alimentacaoVariada = models.CharField(max_length=80, choices=ALIMENTACAO_VARIADA_CHOICES)
    ambienteAdaptado = models.CharField(max_length=80, choices=AMBIENTE_ADAPTADO_CHOICES)
    seguraCasa = models.CharField(max_length=80, choices=SEGURA_CASA_CHOICES)
    dispositivosApoio = models.CharField(max_length=80, choices=DISPOSITIVOS_APOIO_CHOICES)
    nQuedas = models.PositiveIntegerField(null=True, blank=True)
    quedasLesao = models.CharField(max_length=80, choices=QUEDAS_LESOES_CHOICES)
    tabagismo = models.CharField(max_length=80, choices=TABAGISMO_CHOICES)
    alcool = models.CharField(max_length=80, choices=ALCOOL_CHOICES)
    atividadeFisica = models.CharField(max_length=80, choices=ATIVIDADE_FISICA_CHOICES)
    saudeBucal = models.CharField(max_length=80, choices=SAUDE_BUCAL_CHOICES)
    consultasOdonto = models.CharField(max_length=80, choices=CONSULTAS_ODONTO_CHOICES)
    dificuldadesAuditivas = models.CharField(max_length=80, choices=DIFICULDADES_AUDITIVAS_CHOICES)
    visaoInterfere = models.CharField(max_length=80, choices=VISAO_INTERFERE_CHOICES)

    # === HISTÓRICO MÉDICO ===
    doencasCronicas = models.JSONField(default=list, verbose_name="Histórico de Doenças")
    outraDoencaCronica = models.CharField(max_length=100, null=True, blank=True)

    internacoes = models.CharField(
        max_length=50,
        choices=[
            ('Sim, uma vez', 'Sim, uma vez'),
            ('Sim, duas ou mais vezes', 'Sim, duas ou mais vezes'),
            ('Não', 'Não'),
        ],
        verbose_name="Internações hospitalares (último ano)"
    )

    # === VACINAS ===
    vacinacao = models.JSONField(default=list, verbose_name="Vacinação (últimos 12 meses)")

    # === FUNCIONAIS E ATIVIDADES ===
    autocuidado = models.JSONField(default=list, verbose_name="Atividades de Autocuidado")
    atividadesDomesticas = models.JSONField(default=list, verbose_name="Atividades Domésticas")
    atividadesSociaisLazer = models.JSONField(default=list, verbose_name="Atividades Sociais e Lazer")
    mobilidade = models.JSONField(default=list, verbose_name="Mobilidade")
    funcoesCognitivas = models.JSONField(default=list, verbose_name="Funções Cognitivas")

    atividadesSociais = models.JSONField(default=list, verbose_name="Atividades Sociais de Entretenimento")
    atividadesLazer = models.JSONField(default=list, verbose_name="Atividades de Lazer")
    atividadesCulturais = models.JSONField(default=list, verbose_name="Atividades Culturais")
    atividadesFisicasRecreativas = models.JSONField(default=list, verbose_name="Atividades Físicas Recreativas")
    atividadesFamiliares = models.JSONField(default=list, verbose_name="Atividades Familiares")
    atividadesVoluntariado = models.JSONField(default=list, verbose_name="Atividades Voluntárias")

    class Meta:
        db_table = 'questionario'
        verbose_name = "Questionário Completo"

    def __str__(self):
        return f"Usuário {self.id_user} ({self.sexo}, {self.idade} anos)"


class Adm(models.Model):
    id_administracao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    def __str__(self):
        return self.nome
