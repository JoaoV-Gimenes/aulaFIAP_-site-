
def media (lista: list = [0]) -> float:
  calculo = sum(lista) / len(lista)
  if len(lista) > 4:
    raise ValueError('A lista possui muitos itens para a execução do programa!')
  return calculo

try:
  notas = [6, 7, 8, 8, 6]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")

except ValueError as e:
  print(e)

else:
  print(resultado)

finally:
  print('A consulta foi encerrada')

##############################################################################################

def caralho(L1, L2):
  try:
    if len(L1) != len(L2):
      return f'a primeira lista tem {len(L1)} elementos e a segunda {len(L2)} elementos, portando alguns elementos serão ignorados'
    nova_lista = [i + j for i, j in zip(L1, L2)]
  except TypeError:
    return 'São aceitos apenas números!'

  else:
    return nova_lista

lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]
print(caralho(lista1, lista2))
  