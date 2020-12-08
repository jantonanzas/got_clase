# Funciones de soporte para el resto

def print_line(char='-', times=90):
    """
    Función que imprime una linea con un caracter determinado repetido tantas veces como se le indique a la función. Por defecto el caracter sera '-' y el numero de veces que se repetirá serán 90
    :param char: str
    :param times: int
    :return: None
    """
    line = char * times
    print(line)

def mensaje_error():
    """
    Impresión de un mensaje de error para cuando la opción seleccionada no se encuentre dentro de las disponibles
    :return: None
    """
    print_line()
    print('El número elegido no es un valor válido')
    print_line()



# Funciones permanentes durante toda la ejecución

def version_juego():
    """
    Imprime el número de versión del juego
    :return: None
    """
    print_line()
    print('Game of Thrones v0.0.4')
    print_line()

def n_cab_juego():
    """
    Función que solicita al jugador el número de cabañas con las que quiere jugar
    :return: int (de 2 a 30)
    """
    frase = 'Con cuantas cabañas quieres jugar? (mínimo 2, máximo 30)'
    n_cab = 0
    while n_cab not in list(range(2, 31)):
        try:
            n_cab = int(input(frase))
            if n_cab not in list(range(2, 31)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            n_cab = 0
    return n_cab

def info_mision(n_cab):
    """
    Imprime la versión del juego y una pequeña explicación introductoria de como funciona
    :return: None
    """
    import textwrap as t

    texto_ini = 'Perteneces a la Guardia de la Noche. ' \
                'Llevas semanas andando al otro lado del muro, en una expedición para detectar posibles salvajes. ' \
                'Llegas a un poblado con ' + str(n_cab) + ' cabañas. ' \
                'Debes elegir en qué cabaña entrarás. ' \
                'Si está vacía podrás descansar, pero corres el riesgo de encontrarte con un salvaje y morir... ' \
                'O peor, podría haber caminantes blancos...'

    print(t.fill(texto_ini, width=90))
    print_line()



# Rellena las cabañas aleatoriamente cada vez que se quiera iniciar un nuevo juego

def rellena_cab(n_cab, tipo_cab):
    """
    Introduce en una lista el número de cabañas con las que se vaya a jugar, rellenandolas aleatoriamente con un tipo de ocupación concreto (Enemigo, Amigo, Vacía , Caminante Blanco y Vidriagon).
    :param n_cab: int (número de cabañas)
    :param tipo_cab: tuple (tipos de ocupación posibles)
    :return: list (cabañas con sus ocupaciones)
    """
    import random as r
    pesos_tipo_cab = (0.3, 0.25, 0.25, 0.1, 0.1)
    cab = r.choices(tipo_cab, weights=pesos_tipo_cab, k=n_cab)
    return cab



# Para jugar una misma partida (con el mismo número de cabañas ya seleccionado)

def continuar_juego():
    """
    Pregunta al jugador si quiere jugar otra partida, guardando el resultado de la pregunta (1 o 0)
    :return: int (0 o 1)
    """
    frase = 'Para jugar otra vez pulsa 1, si no pulsa 0'
    jugar = -1
    while jugar not in list(range(0, 2)):
        try:
            jugar = int(input(frase))
            if jugar not in list(range(0, 2)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            jugar = -1
    if jugar == 0:
        print_line()
        print('Hasta la próxima!')
    print_line()
    return jugar



# Durante el juego puedes elegir cabaña, dependiendo de cual elijas podrás salir y volver a seleccionar otra diferente o incluso la misma

def elegir_cab(n_cab):
    """
    Dependiendo del número de cabañas establecido, se le pregunta al jugador en que número de cabaña quiere entrar. Guardando esa elección
    :param n_cab: int (número de cabañas)
    :return: int (elección del nº de cabaña del jugador)
    """
    frase = 'Por favor, elige una cabaña de la 1 a la ' + str(n_cab) + ' introduciendo directamente el valor:'
    elige_cab = 0
    while elige_cab not in list(range(1, n_cab + 1)):
        try:
            elige_cab = int(input(frase))
            if elige_cab not in list(range(1, n_cab + 1)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            elige_cab = 0
    print_line()
    return elige_cab



# Que ocurre al entrar a la cabaña

def resultado_cab(elige_cab, cab, tipo_cab):
    """
    En función de la ocupación de las cabañas en la lista, la cabaña elegida por el jugador y los tipos de ocupaciones posibles, esta función retorna qué tipo de ocupante tiene la cabaña en la que ha entrado el jugador.
    :param elige_cab: int (elección del nº de cabaña del jugador)
    :param cab: list (cabañas con sus ocupaciones)
    :param tipo_cab: tuple (tipos de ocupación posibles)
    :return: str (con el tipo de ocupación de la cabaña seleccionada por el jugador)
    """
    print('Entrando en la cabaña nº:', elige_cab)
    print_line()

    if cab[elige_cab - 1] == tipo_cab[0]:  # Enemigo
        print('Hay un salvaje en la cabaña')
        interior_cab = tipo_cab[0]
    elif cab[elige_cab-1] == tipo_cab[1]:  # Amigo
        print('Hay un hermano de la Guardia de la Noche en la cabaña! Quizás pueda ayudarte...')
        interior_cab = tipo_cab[1]
    elif cab[elige_cab-1] == tipo_cab[2]:  # Libre
        print('Has encontrado una cabaña libre: Descansa!')
        interior_cab = tipo_cab[2]
    elif cab[elige_cab-1] == tipo_cab[3]:  # Caminante Blanco
        print('Oh no!!! Hay un Caminante Blanco en la cabaña!')
        interior_cab = tipo_cab[3]
    elif cab[elige_cab-1] == tipo_cab[4]:  # Vidriagon
        print('Hay Vidriagon en esta cabaña')
        interior_cab = tipo_cab[4]

    print_line()
    return interior_cab



# Funciones para Cabaña = Salvaje

def batalla_o_no():
    """
    Pregunta al jugador al entrar a una cabaña con un salvaje si quiere atacar o no.
    :return: int (0 o 1)
    """
    frase = 'Quieres atacar? (pulsa 1 para sí, 0 para no)'
    atac_ini = -1
    while atac_ini not in list(range(0, 2)):
        try:
            atac_ini = int(input(frase))
            if atac_ini not in list(range(0, 2)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            atac_ini = -1

    if atac_ini == 1:
        print_line()
        print('Preparate!')
    else:
        print_line()
        print('Eres un desertor, has muerto!')
    print_line()
    return atac_ini

def ataque():
    """
    Una vez a empezado la batalla, pregunta al jugador si desea continuar atacando o prefiere huir
    :return: int (0 o 1)
    """
    frase = 'Si deseas seguir atacando pulsa 1, si prefieres huir pulsa 0:'
    atac = -1
    while atac not in list(range(0, 2)):
        try:
            atac = int(input(frase))
            if atac not in list(range(0, 2)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            atac = -1
    print_line()
    return atac

def habilidad_especial(wild):
    """
    Función en la que se le pregunta al jugador por una frase de batalla para activar su habilidad especial. En función de lo que elija se le restará incialmente unos puntos de salud al salvaje
    :param wild: int (Salud del salvaje)
    :return: int (Salud del salvaje actualizada)
    """
    frase = 'Quieres utilizar una habilidad especial? Di un frase de batalla'
    habilidad = input(frase)
    print_line()
    if habilidad == 'For the Watch!':
        print('Fantasma ha atacado primero al salvaje! Quitándole 5 puntos de salud')
        wild = wild - 5
    else:
        print('Fantasma no ha acudido a tu llamada...')
    print_line()
    return wild

def restar_salud(hit, hit_power, wild, crow_dic):
    """
    Función que con los parámetros de quien golpea y con que fuerza, actualiza los contadores de salud, restando salud al personaje herido. Imprime también con cuanta fuerza ha golpeado el personaje.
    :param hit: str (quién golpea)
    :param hit_power: int (Fuerza del golpe)
    :param wild: int (Salud del salvaje)
    :param crow_dic: dict (Salud y otras características del Guardia de la Noche)
    :return: tuple(dict, int) (con los valores de crow y wild actualizados)
    """
    if hit == 'wild':
        crow_dic['Salud'] = (crow_dic['Salud'] - hit_power)
        print('El salvaje te ha golpeado con una fuerza de', str(hit_power) + '!')
        print_line()
    elif hit == 'crow':
        wild = (wild - hit_power)
        print('Has golpeado con una fuerza de', str(hit_power) + '!')
        print_line()
    return crow_dic, wild

def muerte_o_saludactual(crow_dic, wild):
    """
    Función que imprime un mensaje si ha muerto un personaje (salud < 0) y que imprime la salud de los dos si no ha muerto ninguno. Además devuelve un valor en funcion de si muere alguien o no
    :param crow_dic: dict (Salud y otras características del Guardia de la Noche)
    :param wild: int (Salud del salvaje)
    :return: int (0 o 1)
    """
    if crow_dic['Salud'] <= 0:
        print('El salvaje te ha matado! Has perdido...')
        print_line()
        muerte = 1
    elif wild <= 0:
        print('Has matado al salvaje! Puedes descansar')
        print_line()
        muerte = 1
    else:
        print('Tu salud:', crow_dic['Salud'], '\nSalud del salvaje:', wild)
        print_line()
        muerte = 0
    return muerte

def lucha_v2(crow_dic):
    """
    Procedimiento de lucha, en función de la salud asignada al Guardia de la Noche. Consiste en un ataque y las actualizaciones correspondientes de salud, repetido tantas veces como veces quiera atacar el jugador. Si deja de atacar y abandona la batalla durante la misma sin que muera ninguno de los dos se actualiza la salida de la cabaña a 1, y el guardia sale de la cabaña (actualizando salida a 1).
    :param crow_dic: int (Salud del Guardia de la Noche)
    :return: dict (actualizados los valores del Guardia)
    """
    import random as r
    wild = r.choice(list(range(40, 56)))
    print('El salvaje tiene una salud de', wild)
    print_line()
    wild = habilidad_especial(wild)
    atac = 1
    muerte = 0
    while ((muerte == 0) and (atac == 1)):
        hit = r.choices(['wild', 'crow'], weights=[0.4, 0.6], k=1)[0]
        hit_power = r.choice(list(range(10, 16)))

        crow_dic, wild = restar_salud(hit,hit_power, wild, crow_dic)

        muerte = muerte_o_saludactual(crow_dic, wild)
        if muerte == 0:
            atac = ataque()
            if atac == 0:
                print('Retiradaaa!!')
                crow_dic['Salida'] = 1
                crow_dic['Curacion'] = 0
                print_line()
        elif muerte == 1:
            crow_dic['Salida'] = 0
    return crow_dic

def interior_cab_enemigo(crow_dic):
    """
    Desarrollo general en el interior de una cabaña con un salvaje. Con la función de ataque incial y la función de lucha
    :param crow_dic: dict (Características del Guardia de la Noche)
    :return: dict (Caracteristicas actualizadas)
    """
    atac_ini = batalla_o_no()
    if atac_ini == 1:
        crow_dic = lucha_v2(crow_dic)
    elif atac_ini == 0:
        crow_dic['Salida'] = 0
    return crow_dic



# Funciones para Cabaña = Amigo

def curacion_pocion():
    """
    Función en la que el jugador tiene que decir una contraseña, si la dice correctamente se le otorga una poción grande y si no una pequeña
    :return: int (pocion)
    """
    frase = '- Hola hermano! Te veo exhausto, si quieres una poción grande di la contraseña'
    contraseña = input(frase)
    print_line()
    if contraseña == 'dracarys':
        print('- Correcto! Aquí tines la poción')
        print_line()
        pocion = 15
    else:
        print('- Lo siento, si no sabes la contraseña solo te puedo dar una poción pequeña')
        print_line()
        pocion = 7
    return pocion

def interior_cab_amigo(crow_dic):
    """
    Desarrollo del interior de cabaña amiga. Si ya se ha solicitado dos veces una poción (Curación = 2) sin haber luchado con un salvaje simplemente no hará nada. Solo entrar y salir de la cabaña. De lo contrario se suman los puntos correspondientes de salud de la pocion y se suma 1 al valor de Curación. Y por ultimo se actualiza la salida a 1 para que salga de la cabaña.
    :param crow_dic: dict (Características generales del Guardia)
    :return: dict (actualizado)
    """
    if crow_dic['Curacion'] < 2:
        pocion = curacion_pocion()
        crow_dic['Salud'] = crow_dic['Salud'] + pocion
        print('Recuperaste', pocion, 'puntos de vida, ahora tienes', crow_dic['Salud'])
        print_line()
        crow_dic['Salida'] = 1
        crow_dic['Curacion'] = crow_dic['Curacion'] + 1
    else:
        print('- Se nos han acabado las pociones, vuelve después de alguna batalla a por más')
        print_line()
        crow_dic['Salida'] = 1
    print('Saliendo de la cabaña...')
    print_line()
    return crow_dic



# Funciones para Cabaña = Vidriagon

def coger_vidriagon():
    """
    Se le solicita al jugador la posiblidad de coger o no el Vidriagon, si lo coge retornará un valor de 1 y si no de 0
    :return: int (0 o 1)
    """
    frase = 'Quieres cogerlo? (pulsa 1 para sí, 0 para no)'
    coger_objeto = -1
    while coger_objeto not in list(range(0, 2)):
        try:
            coger_objeto = int(input(frase))
            print_line()
            if coger_objeto not in list(range(0, 2)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            coger_objeto = -1
    if coger_objeto == 0:
        print('Saliendo de la cabaña...')
    elif coger_objeto == 1:
        print('Has obtenido: Vidriagon. Te vendrá bien si te encuentras a un Caminante Blanco')
    print_line()
    return coger_objeto

def interior_cab_vidriagon(crow_dic):
    """
    Desarrollo del interior de cabaña Vidriagon. Ejecuta la función de coger o no el vidriagon, si el jugador lo ha cogido se actualiza el valor de crow_dic a 1. Y la salida a 1 también
    :param crow_dic: dict (Características del Guardia de la Noche)
    :return: dict (crow_dic)
    """
    coger_objeto = coger_vidriagon()
    if coger_objeto == 1:
        crow_dic['Salida'] = 1
        crow_dic['Vidriagon'] = 1
    elif coger_objeto == 0:
        crow_dic['Salida'] = 1
        crow_dic['Vidriagon'] = 0

    return crow_dic



# Funciones para Cabaña = Caminante Blanco

def usar_vidriagon():
    """
    Función que pregunta al jugador si quiere utilizar el vidriagon. En función de si lo utiliza o no (1 o 0) imprimirá un mensaje u otro.
    :return: None
    """
    frase = 'Quieres utilizar el Vidriagon? (pulsa 1 para sí, 0 para no)'
    usar_objeto = -1
    while usar_objeto not in list(range(0, 2)):
        try:
            usar_objeto = int(input(frase))
            print_line()
            if usar_objeto not in list(range(0, 2)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            usar_objeto = -1
    if usar_objeto == 0:
        print('El caminante blanco te ha matado y ahora formas parte del ejercito de los muertos')
    elif usar_objeto == 1:
        print('Has matado al Caminante Blanco con el Vidriagon! Puedes descansar')
    print_line()

def interior_cab_whitewalk(crow_dic):
    """
    Desarrollo del interior de la cabaña Caminante Blanco. Función en la que si el valor de Vidriagon es 0, imprime una frase y si es 1, ejecuta la función usar_vidriagon. En ambos casos actualiza el valor de salida a 0 y retorna crow_dic actualizado
    :param crow_dic: dict
    :return: dict
    """
    if crow_dic['Vidriagon'] == 0:
        print('El caminante blanco te ha matado y ahora formas parte del ejercito de los muertos')
        print_line()
        crow_dic['Salida'] = 0
    elif crow_dic['Vidriagon'] == 1:
        usar_vidriagon()
        crow_dic['Salida'] = 0
    return crow_dic



# Funcion que ejecuta tod0 el procedimiento que ocurre una vez has entrado a una cabaña

def proc_interior_cab(interior_cab, crow_dic, tipo_cab):
    """
    En función de el tipo de ocupante de interior_cab ejecuta la función relativa a ese tipo de ocupación, devolviendo el valor actualizado de crow_dic
    :param interior_cab: str (con el tipo de ocupante de la cabaña elegida por el jugador)
    :param crow_dic: dict (Características del Guardia de la Noche)
    :param tipo_cab: tuple (con valores str del tipo de ocupantes)
    :return: dict
    """
    if interior_cab == tipo_cab[0]:  # Enemigo
        crow_dic = interior_cab_enemigo(crow_dic)
    elif interior_cab == tipo_cab[1]:  # Amigo
        crow_dic = interior_cab_amigo(crow_dic)
    elif interior_cab == tipo_cab[3]:  # Caminante Blanco
        crow_dic = interior_cab_whitewalk(crow_dic)
    elif interior_cab == tipo_cab[4]:  # Vidriagon
        crow_dic = interior_cab_vidriagon(crow_dic)
    else:
        crow_dic['Salida'] = 0
    return crow_dic



# Función para entrar y salir de distintas cabañas sin que acabe la partida (permaneciendo los mismos ocupantes de las cabañas y guardando información relativa a la salud del personaje u objetos que posea)

def entrada_salida_cab(n_cab, tipo_cab, cab, crow_dic):
    """
    Desarrollo desde que el jugador elige cabaña hasta que se ejecuta el procedimiento interior de la cabaña. Si al salir se ha actualizado el valor de Vidriagon a 1, la cabaña que lo contenía pasa a ser una cabaña con tipo de ocupante Caminante Blanco. Además si el Valor de Salida está actualizado a 1 en el diccionario crow_dic se vuevlve a repetir el bucle.
    :param n_cab: int(número de cabañas)
    :param tipo_cab: tuple(tipos de ocupación posibles)
    :param cab: list (cabañas con sus ocupaciones)
    :param crow_dic: dict (Características del Guardia de la Noche)
    :return: None
    """
    while crow_dic['Salida'] == 1:
        elige_cab = elegir_cab(n_cab)

        interior_cab = resultado_cab(elige_cab, cab, tipo_cab)

        crow_dic = proc_interior_cab(interior_cab, crow_dic, tipo_cab)

        if crow_dic['Vidriagon'] == 1:
            cab[elige_cab-1] = tipo_cab[3]



# Función para jugar tantas partidas como se quiera, con el mismo número de cabañas (pero diferentes ocupantes cada vez)

def proc_juego(n_cab):
    """
    Desarrollo del juego. Se establecen los valores de tipo cab y juego. una vez entra en el bucle while se rellenan aleatoriamente las cabañas, se establece el diccionario de crow_dic con sus valores iniciales. Si todas las cabañas se han rellenado aleatoriamente con Amigos se acaba la partida y se pregunta al jugador si quiere jugar de nuevo, de lo contrario se ejecuta el procedimiento entrada_salida_cab y por último se le preugnta al jugador si quiere jugar de nuevo, en funvión de lo que se conteste se vuelve a ejecutar el bucle.
    :param n_cab: int (número de cabañas)
    :return: None
    """
    tipo_cab = ('Enemigo', 'Amigo', 'Libre', 'Caminante Blanco', 'Vidriagon')
    jugar = 1
    while jugar == 1:

        cab = rellena_cab(n_cab, tipo_cab)

        crow_dic = {'Salud': 50,
                    'Salida': 1,
                    'Vidriagon': 0,
                    'Curacion': 0
                    }
        if cab.count('Amigo') == len(cab):
            crow_dic['Salida'] = 0
            print('Has tenido suerte y has encontrado un pequeño asentamiento de la Guardia de la Noche. Puedes descansar!')
            print_line()

        entrada_salida_cab(n_cab, tipo_cab, cab, crow_dic)

        jugar = continuar_juego()



# Función que contiene el juego en sí, con el número de cabañas que se selecciona, la información de la misión, y el procedimiento de juego

def got_v004():
    """
    Función global que contiene las impresiones iniciales con la descripción del juego, el número de cabañas con las que quiere jugar el jugador y el procedimiento del juego en sí.
    :return: None
    """

    version_juego()
    n_cab = n_cab_juego()
    info_mision(n_cab)

    proc_juego(n_cab)





if __name__ == '__main__':
    got_v004()


