from rest_framework import viewsets
from escola.models import Course, Student
from .serializer import StudentSerializer, CourseSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """
        Exibindo todos os alunos e alunas
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
        Exibindo todos os cursos
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

