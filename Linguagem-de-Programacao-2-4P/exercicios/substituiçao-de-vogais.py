palavras = input('digite uma palavra: ')
for palavra in palavras:
    if palavra in 'aeiou':
        palavras = palavras.replace(palavra, '*')
print(palavras)