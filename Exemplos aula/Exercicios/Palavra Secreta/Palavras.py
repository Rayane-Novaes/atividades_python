import random


palavras_secretas = ['banana', 'Lindo', 'Tia', 'chapéu', 'riso', 'rico', 'jovem', 'encontro']

chave = str(random.choice(palavras_secretas))
print(chave)
vidas = 3

certos = ''


while True:
    digitada = input('Digite uma letra: ')

    if digitada in chave:
        certos += digitada

    formado_palavra = ''

    for letra in chave:
        if letra in certos:
            formado_palavra += letra
        else:
            formado_palavra += '*'

    print(formado_palavra)

    if formado_palavra == chave:
        print('Terminou')
        break