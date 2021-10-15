from rest_framework import viewsets, generics
from rest_framework import authentication
from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    # indica que é necessário estar autenticado no django para ter acesso aos recursos
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


# ListAPIView => uma view apenas para listar (GET) as infos (sem as opções DELETE/PUT/etc)
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno ou aluna"""

    # indicar o aluno que queremos listar as matriculas
    def get_queryset(self):
        # de todas as matriculas, vamos buscar a que possue o mesmo 'id'
        # recupera o id da requisição (ex: 'aluno/2/matricula' --- recupera o id '/2/')
        # pk == primary key
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando os alunos ou alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer