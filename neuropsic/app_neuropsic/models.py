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
            ('Benefícios sociais', 'Benefícios sociais'),
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
