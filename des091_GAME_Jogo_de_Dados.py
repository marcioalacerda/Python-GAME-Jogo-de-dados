'''Programa onde 4 jogadores joquem um dado e tenham resultados aleatórios.
Guardando esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
dado = dict()
print('-='*15)
print(f'{"VALORES SORTEADOS":^30}')
print('-='*15)
for c in range(0, 4):
    dado[f'jogador{c + 1}'] = randint(1, 6)
for k, v in dado.items():
    sleep(1)
    print(f'   O {k} tirou {v}.')
print('-='*15)
print(f'{"RANKING DOS JOGADORES":^30}')
print('-='*15)
contrank = 1
for v in sorted(dado, key=dado.get):
    sleep(1)
    print(f'   {contrank}º lugar : {v} com {dado[v]}')
    contrank += 1
print('-='*15)
