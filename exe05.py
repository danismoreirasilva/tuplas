tupla = ('ovo', 9.90,
         'leite', 6.90,
         'pao', 2.50,
         'requeijão', 6.50,
         'maça', 8.00)

print(tupla)

print(f'{"Lista de Produtos":=^40}')
for i in range(0, len(tupla), 2):
    print(f'{str(tupla[i]).title():.<15}R$ {tupla[i+1]}')