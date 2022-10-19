# -*- coding: utf:8 -*-

# Este script é a minha primeira tentativa de fazer um script onde coloco o preco
# da gasolina, a distancia do percurso e o consumo de gasolina do carro para,
# finalmente, saber quanto vai custar a trip.

distancia = input('Em kilômetros, qual a distância da cidade? ')

preco_combustivel = input('Qual o preço do litro do combustível? ')

rendimento = input('Quantos kms seu carro faz com 1 litro? ')

pessoas = input('Quantas pessoas, contando com você, irão no carro? ')

pessoas = int(pessoas)

# mexi nesse campo pois tive problemas com o if lá de baixo aqui.
# Descobri que precisava transformar esse "string" em um número. No caso usei o INT, todavia CREIO
# que poderia ter usado o float.

litros = (float(distancia)) / (float(rendimento))   #aqui aprendi que não posso usar INT, pq INT é
                                                    #somente para números inteiros. Por isso usei
                                                    #FLOAT

custo_total = (float(litros)) * (float(preco_combustivel)) * (int(2)) #idem aqui. Multipliquei por 2
                                                                      #para incluir a gasolina da volta

custo_total_dividido = (float(custo_total)) / (float(pessoas))

#atribui isto aqui para poder limitar os números
#a duas casas decimais depois, usando round(nome,2 casas)



print()

print('Sua Trip será muito muito especial! ')
print()
print('No total, custará R$', round(custo_total,2), 'de combustível. Ida e volta.')

if pessoas == 1:
    print('Viajar sozinho pode ser muito gostoso, basta escolher boas músicas e bons podcasts!')

else:print("Caso queiram dividir, o valor do combustível será "
           "de R$",round(custo_total_dividido,2),'para cada um.')

total_so_ida = (float(custo_total) / int(2)) #atribui isto aqui para poder limitar os números
                                             #a duas casas decimais depois, usando round(nome,2 casas)

print()
print('PS. Se a sua viagem for somente de ida, o valor do consumo de combustível '
      'será de R$',round(total_so_ida,2),'.')


divisao_so_ida = (float(custo_total)) / (int(2))/ (int(pessoas))

if pessoas > 1:
    print("Nesse caso a divisão pra cada será de R$",round(divisao_so_ida,2),".")

print('Boa viagem!!!!!!!')


