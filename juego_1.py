from random import randint 

posibilidades = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spork']

contador_compu = 0
contador_usuario = 0

print('Gana el primero que llega a tres! Mucha suerte!')

while contador_compu < 5 and contador_usuario < 5:
    if contador_usuario >= 3 or contador_compu >= 3:
        break
    
    compu_move = randint(0,4)
    jugada_compu = posibilidades[compu_move] 
    usuario = input('Rock, Paper, Scissors, Lizard or Spork... ')
    
    if usuario == jugada_compu:
        print('EMPATE!')
        print('Intenta de nuevo!')

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
    
if contador_usuario >= 3:
    print('FELICITACIONES! HAS GANADO!')
    print('Puntajes finales:')
    print('Usuario:', contador_usuario, 'Computador:', contador_compu)
elif contador_compu >= 3:
    print('HAS PERDIDO :(')
    print('Puntajes finales:')
    print('Usuario:', contador_usuario, 'Computador:', contador_compu)