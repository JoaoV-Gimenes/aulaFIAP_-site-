numero = int(print('Digite o número para ser analisado: '))
for i in range(2, numero**0.5):
    if numero%i==0:
        print(f'o número {numero} não é primo')
        break
    else:
        print(f'O número {numero} é primo')