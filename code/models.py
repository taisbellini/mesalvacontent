from django.db import models

class Professor(models.Model):

    cpf = models.CharField(blank=True, max_length=80)
    nome = models.CharField(blank=True, max_length=80)

class ProfessorTarefa(models.Model):
    
    professor = models.ForeignKey(Professor, null=True, blank=True)
    deadline_contrato = models.DateTimeField(auto_now_add=False)
    previsao = models.DateTimeField(auto_now_add=False)
    data_entrega = models.DateTimeField(auto_now_add=False, null=True)
    prontos = models.BooleanField(default=False)
    bonus = models.BooleanField(default=False)

class Plataforma(models.Model):
    
    nome = models.CharField(blank=True, max_length=80)

class Tag(models.Model):

    tag = models.CharField(blank=True, max_length=80)

class Status(models.Model):
    
    status_video = models.IntegerField(default=0)
    status_exercicio = models.IntegerField(default=0)

class Modulo(models.Model):

    nome_modulo = models.CharField(blank=True, max_length=80)
    video = models.ForeignKey(ProfessorTarefa, null=True, blank=True, related_name='modulo_video')
    exercicio = models.ForeignKey(ProfessorTarefa, null=True, blank=True, related_name='modulo_exercicio')
    status = models.ForeignKey(Status, null=True, blank=True)

class Bonus(models.Model):

    avaliacao = models.FloatField(default=0)
    planilha_quadro = models.BooleanField(default=False)
    bonus = models.BooleanField(default=False)

class Aula(models.Model):

    nome = models.CharField(blank=True, max_length=80)
    data = models.DateTimeField(auto_now_add=True)
    gravado = models.BooleanField(default=False)
    upload = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)
    descricao = models.CharField(blank=True, max_length=80)
    comentario = models.CharField(blank=True, max_length=80)
    plataformas = models.ManyToManyField(Plataforma, blank=True)
    modulo = models.ForeignKey(Modulo, null=True, blank=True)
    bonus = models.ForeignKey(Bonus, null=True, blank=True)

class Exercicio(models.Model):

    concluido = models.BooleanField(default=False)
    inserido = models.BooleanField(default=False)
    revisado = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    aula = models.ForeignKey(Aula, null=True, blank=True)

class Curso(models.Model):

    nome = models.CharField(blank=True, max_length=80)
    materia = models.CharField(blank=True, max_length=80)
    categoria = models.CharField(blank=True, max_length=80)
    modulos = models.ManyToManyField(Modulo, blank=True)







