tupla = ('um', 'dois', 'tres', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    while True:
        try:
            num = int(input('Digite um número entre 1 e 10: '))
            if 1 <= num <= 10:
                break
            else:
                print('Erro, tente novamente. ', end='')
        except Exception as e:
            print(f'Erro -> {e}')

    print(f'Você digitou o número: {tupla[num-1]}!')

    while True:
        resp = str(input('Deseja continuar "s" ou "n": ')).lower().strip()
        if resp in 'sn':
            break
        else:
            print(f'Erro -> Digite somente s ou n!')

    if resp == 'n':
        print('Você saiu do programa')
        break