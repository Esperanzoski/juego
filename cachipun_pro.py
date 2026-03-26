from random import randint 

posibilidades = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spork']

contador_compu = 0
contador_usuario = 0

while contador_compu < 3 and contador_usuario < 3:
    if contador_usuario >= 3 or contador_compu >= 3:
        break