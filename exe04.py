
tupla = (int(input('Digite o 1º num: ')),
         int(input('Digite o 2º num: ')),
         int(input('Digite o 3º num: ')),
         int(input('Digite o 4º num: ')))

print(f'O número 5 apareceu {tupla.count(5)} vez(es).')
try:
    print(f'O número 7 apareceu na posição: {tupla.index(7)+1}')
except:
    print(f'O número 7 não foi digitado.')

listaPares = []
for i in tupla:
    if i % 2 == 0:
        listaPares.append(i)

if len(listaPares) > 0:
    print(f'Os números pares foram: {listaPares}')
else:
    print(f'Nenhum número par foi digitado')

