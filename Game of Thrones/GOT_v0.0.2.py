def print_line():
    line = '-'*70
    print(line)

def info_mision():
    import textwrap as t

    print_line()
    print('Game of Thrones v0.0.2')
    print_line()

    texto_ini = 'Perteneces a la Guardia de la Noche. ' \
                'Llevas semanas andando al otro lado del muro, en una expedición para detectar posibles salvajes. ' \
                'Llegas a un poblado con 5 cabañas. ' \
                'Debes elegir en qué cabaña entrarás. ' \
                'Si está vacía podrás descansar... pero corres el riesgo de encontrarte con un salvaje y morir...'

    print(t.fill(texto_ini, width=70))
    print_line()

def rellena_cab(n_cab, tipo_cab):
    import random as r
    cab = r.choices(tipo_cab, k=n_cab)
    return cab

def continuar_juego():
    jugar = input('Para seguir jugando pulsa 1, si no, pulsa cualquier otro valor:')
    print_line()
    if jugar == '1':
        jugar = 1
    else:
        jugar = 0
        print('Hasta la próxima!!')
        print_line()
    return jugar

def mensaje_error():
    print_line()
    print('El número de cabaña no es un valor válido')
    print_line()

def elegir_cab(n_cab):

    frase = 'Por favor, elige una cabaña de la 1 a la ' + str(n_cab) +' , introduciendo directamente el valor:'

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
    print_line()
    print('Entrando en la cabaña nº:', elige_cab)
    print_line()

    if cab[elige_cab - 1] == tipo_cab[0]:
        print('Has perdido! Un salvaje acaba de matarte')
    else:
        print('Has encontrado una cabaña: Descansa!')

    print_line()












def got_v002():

    n_cab = 6
    tipo_cab = ('Enemigo', 'Amigo', 'Vacía')
    cab = rellena_cab(n_cab, tipo_cab)
    jugar = 1

    info_mision()

    while jugar == 1:

        elige_cab = elegir_cab(n_cab)

        resultado_cab(elige_cab, cab, tipo_cab)

        jugar = continuar_juego()

    return cab



got_v002()
