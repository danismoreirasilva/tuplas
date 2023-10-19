tupla = ('python', 'java', 'c++', 'javascript')
tuplaVogais = ('a', 'e', 'i', 'o', 'u')

print(f'{"Analisando cada palavra da tupla":=^60}')
for palavra in tupla:
    i = 0
    print(f'Na palavra "{palavra.upper()}" as vogais são: ', end=' ')
    for letra in palavra:
        if letra.lower() in tuplaVogais:
            print(f'{letra}', end=' ')
        else:
            i += 1
    if i == len(palavra):
        print(f'Ops! Ela não contém vogais!', end=' ')
    print()
