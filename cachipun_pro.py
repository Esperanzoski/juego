from random import randint 

posibilidades = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spok']

contador_compu = 0
contador_usuario = 0

while contador_compu < 3 and contador_usuario < 3:
    if contador_usuario >= 3 or contador_compu >= 3:
        break
    
    mov_compu = randint(0,4)
    jugada_compu = posibilidades[mov_compu]
    usuario = input('Rock, Paper, Scissors, Lizard or Spok... ')
    
    if usuario == jugada_compu:
        print('EMPATARON!')
        print('Intenta de nuevo!')
        print('hola')