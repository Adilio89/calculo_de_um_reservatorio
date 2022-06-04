"""MEU ESTUDO DE PYTHON"""

print('Cálculo De Volume De Um Reservatório')

comprimento = float(input('Entre com o comprimento em metros do reservatório: '))
largura = float(input('Entre com a largura em metros do reservatório: '))
profundidade = float(input('Entre com a profundidade em metros do reservatório: '))

volume_em_m3 = comprimento * largura * profundidade
volume_em_litros = volume_em_m3 * 1000
print('A caixa d\'água comporta %.2f litros.' % volume_em_litros)