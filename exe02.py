serieA = ('Botafogo','Bragantino','Grêmio','Palmeiras','Flamengo','Fluminense','Atlético-MG',\
         'Athletico-PR','Fortaleza','São Paulo','Cuiabá','Cruzeiro','Corinthians','Internacional',\
         'Santos','Goiás','Vasco','Bahia','América-MG','Coritiba')

print(f'Os 6 primeiros colocados são: {serieA[:6]}')
print(f'Os 4 últimos colocados são: {serieA[-4:]}')
print(f'O Fortaleza está na {serieA.index("Fortaleza")+1}º posição!')
print(f'Em ordem alfabética os times são: {sorted(serieA)}')
print(serieA)


