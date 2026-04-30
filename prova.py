import numpy as np
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
gabarito = np.array(['D', 'A', 'B', 'C', 'A'])
def avaliador(lista, gabarito):
  permitidos = np.array(['A', 'B', 'C', 'D'])
  for e in lista:
    if not np.all(np.isin(e, permitidos)):
      print('Está lista possui elementos inválidos!')
    else: 
      nota = np.sum(e == gabarito)
      print(f'{nota}/{len(gabarito)}')
    
print(avaliador(testes_com_ex, gabarito))