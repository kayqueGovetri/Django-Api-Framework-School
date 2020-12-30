from django.contrib import admin
from escola.models import Course, Student
# Register your models here.


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(Student, Students)


class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description', 'level')
    list_display_links = ('id', 'description')
    search_fields = ('description',)
    list_per_page = 20


admin.site.register(Course, Courses)
