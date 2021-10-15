from django.db import models
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

# ModelSerializer => pois já temos um modelo, queremos 'serializar' este modelo
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        
        # '__all__' indica todos os campos do Curso
        fields = '__all__'
        

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula

        # exclude => traz todos os campos exceto o que é indicado
        # se nada é indicado, então todos os campos serão indicados
        exclude = []
        

# Tem a responsabilidade de listar as matriculas de um aluno
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):

    # lê a prop 'curso.descricao' do recurso 'curso'
    # indicando que queremos serializar/exibir a descrição do curso no campo 'curso'
    # no lugar de exibir como '3' (id do curso), será exibida a descrição do curso'
    curso = serializers.ReadOnlyField(source='curso.descricao')

    # indica que sera utilizado um metodo para exibição do periodo (get_period)
    # no lugar de exibir como 'N', será exibido como 'Noturno'
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    # https://cursos.alura.com.br/forum/topico-o-que-e-o-obj-de-onde-ele-vem-123235
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno']

    # def get_periodo(self, obj):
    #     return obj.get_periodo_display()
