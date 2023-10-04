from django.db import models

# Create your models here.

class Turma(models.Model):
    codigo_da_turma = models.CharField(max_length=20)
    
    def __str__(self):
        return self.codigo_da_turma
    

class Turnos(models.Model):
    TURNO_CHOICES = (
        ('M', 'MANHA'),
        ('T', 'TARDE'),
        ('N', 'NOITE'),
        ('I', 'INTEGRAL')
    )
    
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)

    def __str__(self):
        return self.turno
    
class CodigoAluno(models.Model):
    codigo_do_aluno = models.IntegerField()
    
    def __str__(self):
        return str(self.codigo_do_aluno)
    
class Responsavel(models.Model):
    nome_responsavel = models.CharField(max_length=200)
    RG = models.IntegerField()
    cpf = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome_responsavel}'
    
class CadastroAluno(models.Model):
    nome = models.CharField(max_length=200)
    data_de_nascimento = models.DateField()
    RG = models.IntegerField()
    CPF = models.IntegerField()
    
    nome_responsavel = models.CharField(max_length=200)
     
    #chaves
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    turno = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    codigo_do_aluno = models.ForeignKey(CodigoAluno, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome}'
    
    
