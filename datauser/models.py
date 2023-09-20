from django.db import models
from registration.models import User
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField

# Create your models here.
class Stack(models.Model):
    name_stack =  models.CharField(verbose_name='Nombre de Stack', max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Stack"
        verbose_name_plural = "Tecnicas Usadas"

    def __str__(self):
        return f'{self.name_stack}'
    
class ProjectDev(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    stack = models.ManyToManyField(Stack, verbose_name="Tecnologias Usadas")
    name_project = models.CharField(verbose_name='Nombre de Proyecto', max_length=100)
    resume_project = models.TextField(verbose_name='Descripcion')
    url_repo = models.URLField(verbose_name='Url Repositorio')
    year_production = models.PositiveIntegerField(verbose_name='Año en Producción', null=True, blank=True)
    developing = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Proyectos Desarrollados'

    def __str__(self) :
        return f'{self.name_project}'
    
class EmploymentHistory(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    stack = models.ManyToManyField(Stack, verbose_name="Tecnologias Usadas")
    company = models.CharField(verbose_name='Empresa',max_length=256)
    position = models.CharField(verbose_name='Cargo', max_length=150)
    job_description = RichTextField(verbose_name='Funciones Desempeñadas')
    start_date = models.DateField(verbose_name='Fecha de Inicio')
    end_date = models.DateField(verbose_name='Fecha de Culminación', null=True, blank=True)
    still_work = models.BooleanField(default=False, verbose_name='Aún trabajo allí')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Historia Laboral'

    def __str__(self):
        return f'{self.company} - {self.position}'
    
class Academy(models.Model):
    ESTUDIOS = [
        ("Primaria","Primaria"),
        ("Bachillerato","Bachillerato"),
        ("Curso","Curso"),
        ("Tecnico","Tecnico"),
        ("Tecnologo", "Tecnologo"),
        ("Pregrado","Pregrado"),
        ("Posgrado", "Posgrado"),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    type_degree = models.CharField(verbose_name='Tipo de Educación', choices=ESTUDIOS, max_length=150)
    academy_name = models.CharField(verbose_name='Institución Educativa', max_length=150)
    degree_obtained = models.CharField(verbose_name='Grado Obtenido',  max_length=50)
    degree_esp = models.CharField(verbose_name='Especialidad del Grado',  max_length=50, null=True, blank=True)
    start_date = models.DateField(verbose_name='Fecha de Inicio de Estudios', null=True, blank=True)
    finish_date = models.DateField(verbose_name='Fecha de Graduación', null=True, blank=True)
    in_progress = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Formacion Académica"

    def __str__(self) -> str:
        if self.finish_date is None:
            return f'{self.degree_obtained} - en Progreso'
        else:
            return f'{self.degree_obtained} - {self.finish_date}'
        
class HobbiesExtras(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    hobby = models.CharField(verbose_name='Afición/Pasatiempo', max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Hobbies - Extras'

    def __str__(self):
        return f'{self.hobby}'
    
class Skills(models.Model):
    LEVEL = [
        ('Basico','Basico'),
        ('Intermedio','Intermedio'),
        ('Alto','Alto'),
        ('Avanzado','Avanzado')
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    skill = models.CharField(verbose_name='Competencias', max_length=100)
    level = models.CharField(verbose_name='Nivel', choices=LEVEL, max_length=100)
    description = models.TextField(verbose_name='Descripcion') #descripcion detallada del nivel y habilidades adquiridas
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f'{self.skill} - {self.level}'
    

class Facts(models.Model):
    TYPE_FACT=[
        ('Clientes','Clientes'),
        ('Proyectos','Proyectos'),
        ('Horas de Soporte','Horas de Soporte'),
        ('Hard Workers','Hard Workers'),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    fact = models.CharField(verbose_name='Hechos', max_length=25, choices=TYPE_FACT)
    value = models.PositiveIntegerField(verbose_name='Total')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Hechos'

    def __str__(self):
        return f'{self.fact}'