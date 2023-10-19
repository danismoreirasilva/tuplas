from random import randint


tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Tupla gerada: {tupla}')

print(f'Os números gerados foram: ',end='' )
for i in tupla:
    print(f'{i}', end=' ')
print()
print(f' O maior elemento é {max(tupla)}')
print(f' O menor elemento é {min(tupla)}')
print(f' A soma dos elementos é {sum(tupla)}')