def print_line(char='-', times=90):
    """
    Función que imprime una linea con un caracter determinado repetido tantas veces como se le indique a la función. Por defecto el caracter sera '-' y el numero de veces que se repetirá serán 90
    :param char: str
    :param times: int
    :return: None
    """
    line = char*times
    print(line)

def info_mision():
    """
    Imprime la versión del juego y una pequeña explicación introductoria de como funciona
    :return: None
    """
    import textwrap as t

    print_line()
    print('Game of Thrones v0.0.3')
    print_line()

    texto_ini = 'Perteneces a la Guardia de la Noche. ' \
                'Llevas semanas andando al otro lado del muro, en una expedición para detectar posibles salvajes. ' \
                'Llegas a un poblado con 5 cabañas. ' \
                'Debes elegir en qué cabaña entrarás. ' \
                'Si está vacía podrás descansar... pero corres el riesgo de encontrarte con un salvaje y morir...'

    print(t.fill(texto_ini, width=90))
    print_line()

def rellena_cab(n_cab, tipo_cab):
    """
    Introduce en una lista el número de cabañas con las que se vaya a jugar, rellenandolas aleatoriamente con un tipo de ocupación concreto (Enemigo, Amigo, Vacía).
    :param n_cab: int (número de cabañas)
    :param tipo_cab: tuple (tipos de ocupación posibles)
    :return: list (cabañas con sus ocupaciones)
    """
    import random as r
    cab = r.choices(tipo_cab, k=n_cab)
    return cab

def mensaje_error():
    """
    Impresión de un mensaje de error para cuando la opción seleccionada no se encuentre dentro de las disponibles
    :return: None
    """
    print_line()
    print('El número elegido no es un valor válido')
    print_line()

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

def elegir_cab(n_cab):
    """
    Dependiendo del número de cabañas establecido, se le pregunta al jugador en que número de cabaña quiere entrar. Guardando esa elección
    :param n_cab: int (número de cabañas)
    :return: int (elección del nº de cabaña del jugador)
    """
    frase = 'Por favor, elige una cabaña de la 1 a la ' + str(n_cab) +' introduciendo directamente el valor:'
    elige_cab = 0
    while elige_cab not in list(range(1, n_cab+1)):
        try:
            elige_cab = int(input(frase))
            if elige_cab not in list(range(1, n_cab+1)):
                mensaje_error()
        except ValueError:
            mensaje_error()
            elige_cab = 0
    print_line()
    return elige_cab

def resultado_cab(elige_cab, cab, tipo_cab):
    """
    En función de la ocupación de las cabañas en la lista, la cabaña elegida por el jugador y los tipos de ocupaciones posibles, esta función retorna un valor de 0 si no hay un salvaje en ella o de 1 si hay un salvaje.
    :param elige_cab: int (elección del nº de cabaña del jugador)
    :param cab: list (cabañas con sus ocupaciones)
    :param tipo_cab: tuple (tipos de ocupación posibles)
    :return: int (0 o 1)
    """
    print('Entrando en la cabaña nº:', elige_cab)
    print_line()

    if cab[elige_cab-1] == tipo_cab[0]:
        print('Hay un salvaje en la cabaña')
        interior_cab = 'Enemigo'
    else:
        print('Has encontrado una cabaña libre de enemigos: Descansa!')
        interior_cab = ''

    print_line()
    return interior_cab

def batalla_o_no():
    """
    Pregunta al jugador al entrar a una cabaña con un salvaje si quiere atacar o no
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

# Antigua version de lucha


 # def lucha(crow):
 #    import random as r
 #    wild = r.choice(list(range(40, 56)))
 #    atac = 1
 #
 #    while ((wild > 0) and (crow > 0) and (atac == 1)):
 #        hit = r.choices(['wild', 'crow'], weights=[0.4, 0.6], k=1)[0]
 #        hit_power = r.choice(list(range(10, 16)))
 #        if hit == 'wild':
 #            crow = (crow - hit_power)
 #            if crow <= 0:
 #                print('El salvaje te ha matado')
 #                print_line()
 #                atac = 0
 #            elif crow > 0:
 #                print('El salvaje te ha golpeado con una fuerza de', hit_power, ', te quedan', crow, 'puntos de salud')
 #                print_line()
 #                atac = ataque()
 #                if atac == 0:
 #                    print('Has muerto por cobarde')
 #                    print_line()
 #        elif hit == 'crow':
 #            wild = (wild - hit_power)
 #            if wild <= 0:
 #                print('Has matado al salvaje! Puedes descansar')
 #                print_line()
 #                atac = 0
 #            elif wild > 0:
 #                print('Has golpeado con una fuerza de', str(hit_power)+'!', 'Al salvaje le quedan', wild, 'puntos de salud')
 #                print_line()
 #                atac = ataque()
 #                if atac == 0:
 #                    print('Has muerto por cobarde')
 #                    print_line()

def restar_salud(hit, hit_power, wild, crow):
    """
    Función que con los parámetros de quien golpea y con que fuerza, actualiza los contadores de salud, restando salud al personaje herido. Imprime también con cuanta fuerza ha golpeado el personaje.
    :param hit: str (quién golpea)
    :param hit_power: int (Fuerza del golpe)
    :param wild: int (Salud del salvaje)
    :param crow: int (Salud del Guardia de la Noche)
    :return: tuple(int, int) (con los valores de crow y wild actualizados)
    """
    if hit == 'wild':
        crow = (crow - hit_power)
        print('El salvaje te ha golpeado con una fuerza de', str(hit_power) + '!')
        print_line()
    elif hit == 'crow':
        wild = (wild - hit_power)
        print('Has golpeado con una fuerza de', str(hit_power) + '!')
        print_line()
    return crow, wild

def muerte_o_saludactual(crow, wild):
    """
    Función que imprime un mensaje si ha muerto un personaje (salud < 0) y que imprime la salud de los dos si no ha muerto ninguno. Además devuelve un valor en funcion de si muere alguien o no
    :param crow: int (Salud del Guardia de la Noche)
    :param wild: int (Salud del salvaje)
    :return: int (0 o 1)
    """
    if crow <= 0:
        print('El salvaje te ha matado! Has perdido...')
        print_line()
        muerte = 1
    elif wild <= 0:
        print('Has matado al salvaje! Puedes descansar')
        print_line()
        muerte = 1
    else:
        print('Tu salud:', crow, '\nSalud del salvaje:', wild)
        print_line()
        muerte = 0
    return muerte

def lucha_v2(crow):
    """
    Procedimiento de lucha, en función de la salud asignada al Guardia de la Noche. Consiste en un ataque y las actualizaciones correspondientes de salud, repetido tantas veces como veces quiera atacar el jugador. O hasta que muera uno de los personajes
    :param crow: int (Salud del Guardia de la Noche)
    :return: None
    """
    import random as r
    wild = r.choice(list(range(40, 56)))
    print('El salvaje tiene una salud de', wild)
    print_line()
    atac = 1
    muerte = 0
    while ((muerte == 0) and (atac == 1)):
        hit = r.choices(['wild', 'crow'], weights=[0.4, 0.6], k=1)[0]
        hit_power = r.choice(list(range(10, 16)))

        salud_actualizada = restar_salud(hit,hit_power, wild, crow)
        crow = salud_actualizada[0]
        wild = salud_actualizada[1]

        muerte = muerte_o_saludactual(crow, wild)
        if muerte == 0:
            atac = ataque()
            if atac == 0:
                print('Has muerto por cobarde')
                print_line()

def proc_interior_cab(interior_cab, crow):

    if interior_cab == 'Enemigo':
        atac_ini = batalla_o_no()
        if atac_ini == 1:
            lucha_v2(crow)
        else:
            pass
    else:
        pass

def proc_juego(n_cab, tipo_cab):
    jugar = 1
    while jugar == 1:

        cab = rellena_cab(n_cab, tipo_cab)

        crow = 50

        elige_cab = elegir_cab(n_cab)

        interior_cab = resultado_cab(elige_cab, cab, tipo_cab)

        proc_interior_cab(interior_cab, crow)

        jugar = continuar_juego()

def got_v003():

    n_cab = 5
    tipo_cab = ('Enemigo', 'Amigo', 'Vacía')

    info_mision()

    proc_juego(n_cab, tipo_cab)



got_v003()


