frase = input('Insira uma frase: ').lower().split()
palavras = {

}
for palavra in frase:
    if palavra in palavras:
        palavras[palavra] += 1
    else:
        palavras[palavra] = 1

print(palavras)