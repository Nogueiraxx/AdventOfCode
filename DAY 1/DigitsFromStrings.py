#! Funciona para chaves que contem apenas números, 
#o input do desafio envolve strings que contem numero por extenso ex: 
#five3 e que nesse caso isso representa 53.
def BuscarDigito(frases):
    for i in range(len(frases)):
        character = frases[i]
        if character.isdigit():
            soma = character
            return soma


def abrirDoc():
    with open('DAY 1\CalibrationDoc.txt') as arq:
        linhas = arq.readlines()
    keys = []

    for i in range(len(linhas)):
        charact = linhas[i]
        keys.append(charact)
    return keys


chaves = abrirDoc()
truncado = ''
somatorio = 0
for key in chaves:
    frases = [key]
    frases.append(key[::-1])
    truncado = BuscarDigito(frases[0]) + BuscarDigito(frases[1])
    somatorio += int(truncado)

print(somatorio)



