from datetime import datetime

def get_edad(fecha_nacimiento):

    try:
        if datetime.now().month <= fecha_nacimiento.month and datetime.now().day <= fecha_nacimiento.day:
            # Si el mes y el día actual es menor o igual al del nacimiento
            edad = (datetime.now().year-1) - fecha_nacimiento.year
        else:
            edad = datetime.now().year - fecha_nacimiento.year
    except:
        edad = 'No es posible calcular la edad'

    return edad
