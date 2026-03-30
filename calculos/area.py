import unicodedata

def normalizar(texto):
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8').lower()

def area_retangulo():
    altura = int(input('Digite o valor da altura do Retângulo: '))
    base = int(input('Digite o valor da base do Retângulo: '))
    return f'O valor da área do Retângulo é: {altura * base}'

def area_circulo():
    raio = int(input('Digite o valor do raio do Círculo: '))
    return f'O valor da área do Círculo é: {raio**2 * 3.14}'

def area_triangulo():
    altura = int(input('Digite o valor da altura do Triângulo: '))
    base = int(input('Digite o valor da base do Triângulo: '))
    return f'O valor da área do Triângulo é: {(altura * base) / 2}'

def area_esfera():
    raio = int(input('Digite o valor do raio da Esfera: '))
    return f'O valor da área da Esfera é: {4 * (raio**2) * 3.14}'

def volume_retangulo():
    altura = int(input('Digite o valor da altura do Retângulo: '))
    base = int(input('Digite o valor da base do Retângulo: '))
    comprimento = int(input('Digite o valor do comprimento do Retângulo: '))
    return f'O valor da área do Retângulo é: {altura * base * comprimento}'

def volume_triangulo():
    altura = int(input('Digite o valor da altura do Triângulo: '))
    base = int(input('Digite o valor da base do Triângulo: '))
    comprimento = int(input('Digite o valor do comprimento do Triângulo: '))
    return f'O valor da área do Triângulo é: {(altura * base* comprimento) / 2}'

def volume_esfera():
    raio = int(input('Digite o valor do raio da Esfera: '))
    return f'O valor da área da Esfera é: {(4 * (raio**3) * 3.14)/3}'

def sair():
    print("Saindo do programa...")
    exit()

calculo = {
    'retangulo_area': area_retangulo,
    'triangulo_area': area_triangulo,
    'circulo_area': area_circulo,
    'esfera_area': area_esfera,
    'retangulo_volume' : volume_retangulo,
    'triangulo_volume' : volume_triangulo,
    'esfera_volume' : volume_esfera,
    'sair': sair
}

while True:
    solicitacao = normalizar(input('Qual a forma geométrica do objeto? Deseja calcular a área ou o valoume? (ex: forma_area / forma_volume): '))
    funcao = calculo.get(solicitacao)
    if funcao:
        resultado = funcao()
        if resultado:         # sair() retorna None, então não tenta printar
            print(resultado)
    else:
        print('Forma geométrica inválida!')