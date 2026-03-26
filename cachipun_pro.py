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
        print('Empate')
        print('Intenta de nuevo!')
        print('Chao')

    elif jugada_compu == 'Spork' and (usuario == 'Scissors' or usuario == 'Rock'):
        contador_compu += 1
        print('PERDISTE ESTA RONDA :(')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)  
    elif jugada_compu == 'Lizard' and (usuario == 'Spork' or usuario == 'Paper'):
        contador_compu += 1
        print('PERDISTE ESTA RONDA :(')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif jugada_compu == 'Rock' and (usuario == 'Lizard' or usuario == 'Scissors'):
        contador_compu += 1
        print('PERDISTE ESTA RONDA :(')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif jugada_compu == 'Paper' and (usuario == 'Rock' or usuario == 'Spork'): #REVISAR 
        contador_compu += 1
        print('PERDISTE ESTA RONDA :(')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)          
    elif jugada_compu == 'Scissors' and (usuario == 'Paper' or usuario == 'Lizard'):
        contador_compu += 1
        print('PERDISTE ESTA RONDA :(')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)  
        
    elif usuario == 'Spork' and (jugada_compu == 'Scissors' or jugada_compu == 'Rock'):
        contador_usuario += 1
        print('GANASTE ESTA RONDA!')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif usuario == 'Lizard' and (jugada_compu == 'Spork' or jugada_compu == 'Paper'):
        contador_usuario += 1
        print('GANASTE ESTA RONDA!')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif usuario == 'Rock' and (jugada_compu == 'Lizard' or jugada_compu == 'Scissors'):
        contador_usuario += 1
        print('GANASTE ESTA RONDA!')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif usuario == 'Paper' and (jugada_compu == 'Rock' or jugada_compu == 'Spork'):
        contador_usuario += 1
        print('GANASTE ESTA RONDA!')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
    elif usuario == 'Scissors' and (jugada_compu == 'Paper' or jugada_compu == 'Lizard'):
        contador_usuario += 1
        print('GANASTE ESTA RONDA!')
        print('Usuario:', contador_usuario, 'Computador:', contador_compu)
