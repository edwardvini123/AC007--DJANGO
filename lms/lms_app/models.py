from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        if(self.login == ''):
            raise Exception('login nao enviado')
        if self.email == None or self.email == '':
            self.email = 'email nao fornecido'
        Professor_login = Professor.objects.filter(login=self.login)
        if len(Professor_login) > 0:
            raise Exception('login ja existente')
        print("ESTOU SALVANDO")
        super(Professor,self).save()   
       

class Disciplina(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Ementa: " + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)

    def save(self):
        Disciplina_duplicada = Disciplina.objects.filter(nome=self.nome)
        if len(Disciplina_duplicada) > 0:
            raise Exception('Disciplina Duplicada')
        super(Disciplina,self).save() 

class DisciplinaOfertada(models.Model):
    def __str__(self):
        return "Curso: " + self.curso + "Ano: " + self.ano + "Semestre: " + self.semestre + "Turma: " + self.turma + "Professor: " + self.Professor + "Disciplina: " + self.Disciplina

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField()#um inteiro, representa um ano
    semestre = models.IntegerField()#um inteiro, 1 para primeiro sem e 2 para segundo 
    professor = models.IntegerField()#id de um professor valido
    disciplina = models.IntegerField()#id de um professor valida

    def save(self):
        if not (self.curso == "ADS" or self.curso == "SI" or self.curso == "BD"):
            raise Exception('Disciplina Incorreta')
        DisciplinaOfertada_duplicada = DisciplinaOfertada.objects.filter(curso=self.curso,ano=self.ano,semestre=self.semestre,turma=self.turma,professor=self.professor,disciplina=self.disciplina)
        if len(DisciplinaOfertada_duplicada) > 0:
            raise Exception('Disciplina Duplicada')
        super(DisciplinaOfertada,self).save() 



