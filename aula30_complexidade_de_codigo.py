'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local que o carro está na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

veloc_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                       local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and veloc_carro_passou_radar_1

if veloc_carro_passou_radar_1:
    print('O carro ultrapassou a velocidade do radar')

if carro_passou_radar_1:
    print('Carro passou o radar 1')

if  carro_passou_radar_1 and veloc_carro_passou_radar_1:
    print('Carro multado em radar 1')