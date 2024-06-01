#! Funciona para chaves que contem apenas números, o input do desafio envolve strings que contem numero por extenso ex: five3 e que nesse caso isso representa 53.
# def BuscarDigito(frases):
#     soma = 0

#     for frase in frases:
#         for i in range(len(frase)):
#             character = frase[i]
#             if character.isnumeric():
#                 soma += int(character)
#                 break
        
#     return int(soma)


# def abrirDoc():
#     with open('CalibrationDoc.txt') as arq:
#         linhas = arq.readlines()
#     keys = []
#     cont = 0

#     for i in range(len(linhas)):
#         charact = linhas[i]
#         keys.append(charact)

#     return keys

# chaves = abrirDoc()
# somatorio = 0
# for key in chaves:
#     frases = [key]
#     frases.append(key[::-1])
#     somatorio += BuscarDigito(frases[0])
#     somatorio += BuscarDigito(frases[1])

# print(somatorio)


