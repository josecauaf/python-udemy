"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 50 # Velocidade atual do carro
local_carro = 100 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_veiculo_passou_radar_1 = velocidade > RADAR_1
veiculo_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1)
veiculo_multado_radar_1 = veiculo_passou_radar_1 and velocidade_veiculo_passou_radar_1

if velocidade_veiculo_passou_radar_1:
    print(f'[^] VELOCIDADE REGISTRADA: {velocidade}')
    print('[>] Veículo passou da velocidade do radar 1')

if veiculo_passou_radar_1:
    print('Veículo passou do radar 1')

if veiculo_multado_radar_1:
    print('Veículo multado em radar 1')