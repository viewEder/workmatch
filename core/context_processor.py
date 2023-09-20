""" 
    Función de procesador de contexto para mostrar en todos los template html
"""
from registration.models import User

def cpMenu(request):
    usuario = request.user

    menu = {
        "home": "Inicio" ,
        "about":"Acerca de",
        "services":"Servicios",
        "portfolio": "Portafolio",
        "pricing": "Precios",
        "team": "Equipo"
    }
    return menu

def cpUserSign(request):
    # if request.user.username:
    #     # Si el user está logeado, se le envía a la página principal del sitio web
    #     usuario = request.user
    #     print(usuario.first_name)

    #     data = {
    #         "foto" : usuario.photo.url,
    #         "nombre_usuario" : usuario.first_name,
    #         "apellido_usuario":  usuario.last_name
    #     }

    #     return data
    # else :
    #     data = {
    #         "foto" : "usuario.photo.url",
    #         "nombre_usuario" : "usuario.first_name + ' '+ usuario.last_name"
    #     }
    pass

        