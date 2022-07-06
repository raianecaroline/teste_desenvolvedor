# coding=utf-8

import json

f = open('dados.json')

dados = json.load(f)

maior_valor = 0
menor_valor = 100000
media = 0

for i in dados:
    if i['valor'] > maior_valor:
        maior_valor = i['valor']
    if i['valor'] < menor_valor:
        if i['valor'] == 0.0:
            continue
        else:
            menor_valor = i['valor']
    media += i['valor']

media = media / 21
dias_maior_que_media = 0
for i in dados:
    if i['valor'] > media:
        dias_maior_que_media += 1

print('\033[94m' + "\nA média mensal foi:\n" + str(media))
print('\033[93m' + "\nO número de dias que o faturamento mensal foi maior do que a média foi:\n" + str(
    dias_maior_que_media))
print('\033[92m' + "\nO maior faturamento do mês foi\n" + str(maior_valor))
print('\033[91m' + "\nO menor faturamento do mês foi:\n" + str(menor_valor))

f.close()
