from django.contrib import admin

from apkchamada.models import Turma,Turnos, CodigoAluno, CadastroAluno
# Register your models here.
admin.site.register(Turma)
admin.site.register(Turnos)
admin.site.register(CodigoAluno)
admin.site.register(CadastroAluno)
# admin.site.register(Responsavel)
