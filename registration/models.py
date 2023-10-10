from django.db import models
from django.contrib.auth.models import AbstractUser
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField
# Para la actualización de datos de usuario:
from django.dispatch import receiver
from django.db.models.signals import post_save

# # funcion para la carga de imagenes de usuario:
def upload_image(instance, filename):
    return "img/users/{id}/{filename}".format( id = instance.pk, filename = filename)

# Create your models here.
class User(AbstractUser):
    # Coleccion para los tipos de documento de identidad:
    TIPODOCUMENTO_CHOICES= [
        ("CC","Cédula Ciudadania"),
        ("CE","Cedula Extranjeria"),
        ("TI","Tarjeta Identidad"),
        ("PA","Pasaporte"),
        ("RC","Registro civil"),
        ("NN","No Identificado"),
        ("OTRO","Otro")
    ]
    # Sobreescribo el campo'username':
    email = models.EmailField(verbose_name='Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    tipo_id = models.CharField(verbose_name='Tipo de identificación', max_length = 20, choices=TIPODOCUMENTO_CHOICES)
    identification = models.CharField(verbose_name='Número de Identificación', max_length = 20)
    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to=upload_image, null=True, blank=True)
    country = models.CharField(verbose_name= 'Pais', max_length=255)
    city = models.CharField(verbose_name= 'Ciudad ', max_length=255)
    addres = models.CharField(verbose_name= 'Dirección', max_length=255)
    phone = models.CharField(verbose_name= 'Telefono', max_length=255)
    birthday = models.DateField(verbose_name= 'Fecha de Nacimiento', null=True, blank=True)
    ocupation_job = models.CharField(verbose_name= 'Ocupación', max_length=255)
    relocate = models.BooleanField(verbose_name= 'Se puede Desplazar?', default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Links(models.Model):
    TIPO_ENLACE = [
        ('LI','LinkedIn'),
        ('GH','Github'),
        ('WEBSITE','Sitio Web Personal'),
        ('OTHERS','Otros')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    type_link = models.CharField(verbose_name='Tipo de Enlace', max_length=50, choices=TIPO_ENLACE)
    link = models.URLField(verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together=['user','link']
        verbose_name = 'Enlace'
        verbose_name_plural ='Enlaces'

    def __str__(self):
        return f'{self.user}-{self.link}'

class Excerp(models.Model):
    EXCERPTION_TYPE=[   
        (1,'Perfil Profesional'),
        (2,'Objetivo Profesional'),
        (3,'Aptitudinal'),
        (4,"Conocimientos y Habilidades"),
        (5,"Proyectos Realizados"),
        (6,"Experiencia Laboral"),
        (7,"Sumario"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    excerption_type = models.IntegerField(verbose_name='Tipo de Excerpcion', choices=EXCERPTION_TYPE)
    content = RichTextField(verbose_name='Contenido del Articulo')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-created"]
        verbose_name="Articulo"
        verbose_name_plural= "Articulos"

    def __str__(self):
        for item in self.EXCERPTION_TYPE:
            if self.excerption_type == item[0]:
                return f'{self.user} - {item[1]}'


# Metodo de datos Seguros de Usuario:
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        User.objects.get_or_create(id = instance.id) # Traiga el dato del usuario con id = request.user.id
