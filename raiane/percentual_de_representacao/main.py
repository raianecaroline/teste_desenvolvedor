# coding=utf-8

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

TOTAL = SP + RJ + MG + ES + OUTROS

SP_porcentagem = (SP / TOTAL) * 100
print('\033[92m' + "SP representa " + str(SP_porcentagem)[:4] + "%" + " do total!")

RJ_porcentagem = (RJ / TOTAL) * 100
print('\033[92m' + "RJ representa " + str(RJ_porcentagem)[:4] + "%" + " do total!")

MG_porcentagem = (MG / TOTAL) * 100
print('\033[92m' + "MG representa " + str(MG_porcentagem)[:4] + "%" + " do total!")

ES_porcentagem = (ES / TOTAL) * 100
print('\033[92m' + "ES representa " + str(ES_porcentagem)[:4] + "%" + " do total!")
