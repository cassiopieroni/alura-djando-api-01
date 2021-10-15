from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):

    # campos para exibir no admin
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    
    # se quiser alterar um Aluno, deve ser possível clicar nestes campos
    list_display_links = ('id', 'nome')

    # campo de busca (pode buscar por 'nome')
    search_fields = ('nome',)

    # define paginação na quantidade de Alunos
    list_per_page = 20


# registrar as configurações no admin
# 1o arg - modelo usado
# 2o arg - config do model admin
admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):

    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):

    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)
