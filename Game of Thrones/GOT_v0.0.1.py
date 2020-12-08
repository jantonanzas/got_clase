
def got_v001():
    import random as r
    import textwrap as t
    line = '-'*70

    print(line)
    print('Game of Thrones v0.0.1')
    print(line)

    texto_ini = 'Perteneces a la Guardia de la Noche. '\
                'Llevas semanas andando al otro lado del muro, en una expedición para detectar posibles salvajes. '\
                'Llegas a un poblado con 5 cabañas. '\ 
                'Debes elegir en qué cabaña entrarás. '\ 
                'Si está vacía podrás descansar... pero corres el riesgo de encontrarte con un salvaje y morir...'

    print(t.fill(texto_ini, width=70))
    print(line)

    tipo_cab = ('Amigo', 'Enemigo', 'Vacía')
    n_cab = 5
    cab = r.choices(tipo_cab, k=n_cab)
    jugar = '1'

    while (jugar == '1'):

        try:
            elige_cab = int(input('Por favor, elige una cabaña de la 1 a la 5, introduciendo directamente el valor:'))

            if (elige_cab in list(range(1, n_cab+1))):
                print('Entrando en la cabaña nº:', elige_cab)
                if cab[elige_cab-1] == 'Enemigo':
                    print('Has perdido! Un salvaje acaba de matarte')
                else:
                    print('Descansa!')
                jugar = input('Para seguir jugando pulsa 1, si no, pulsa cualquier otro valor:')
            else:
                print('El número de cabaña no es un valor válido')

        except ValueError:
            print('El número de cabaña no es un valor válido')

    return print(cab)



got_v001()









n_cab = 7

seq_n_cab = list(range(1, n_cab + 1))
for i, ncab in enumerate(seq_n_cab):
    seq_n_cab[i] = str(ncab)

