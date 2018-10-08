from django.contrib import admin

# Register your models here.
from lms_app.models import Professor
from lms_app.models import Disciplina
from lms_app.models import DisciplinaOfertada
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(DisciplinaOfertada)