# -*- coding: utf-8 -*-

def atbarras(n, e, l, d, pa):
  '''
  Calcula o valor da resistência em cada barra do aterramento,
  com qualquer número de barras.
  Segue aqui a ordem das variáveis e suas unidades:
  número de barras;
  distância entre as barras em metros;
  comprimento das barras em metros;
  diâmetro das barras em milimetros;
  resistividade aparente em ohms.metro.
  '''

  import numpy as np #Para o log
  import math #Para a raiz quadrada
  π = 3.14159

  ri = {}
  #O cálculo da primeira influência é diferente
  ri[1] = (pa/(2*π*l)) * (np.log( (4*l) / (d*0.001) ))
  #O resto é igual, possibilitando o uso da mesma fórmula
  t = 2
  while t <= n:
    b = math.sqrt(l**2 + (e*(t-1))**2) #não é eficiente criar uma variável para cada barra
    ri[t] = (pa/((4*π)*l)) * (np.log( (((b + l)**2)-((e*(t-1))**2)) / (((e*(t-1))**2)-((b - l)**2)) ))
    t += 1

  r = {}
  #converte o dicionário em uma lista
  calculo = [] #talvez seja possível fazer algumas dessas operações com dicionários mesmo. Assim não ia haver necessidade de ficar convertendo
  t = 1
  while t <= n:
    calculo.append(ri[t])
    t += 1

  #gera e executa as fórmulas da soma
  t = 0
  i = 1 #eu vou precisar que o index do dict aumente em um ritmo diferente do t
  m = n
  while t < n:
    if t != 0: #esse if não deve rodar na primeira vez
      calculo[m] = calculo[t]
      r[i] = sum(calculo)
    else:
      r[i] = sum(calculo)
    t += 1
    m -= 1
    i += 2  #os dicionários realmente brilharam aqui. graças a eles eu pude fazer com que o index seguisse um padrão que não fosse 1, 2, 3...

  #distribui os resultados
  r2 = {}
  t = 1
  if (n % 2) == 1:  #1  3  5  7 <-loop
    while t <= (n): #12 34 56 7! <-valores sendo distribuidos (todos os valores repetem, menos o impar)
      r2[t] = r[t]  #cada resultado aparece duas vezes, por isso o mesmo resultado ocupa dois espaços do dicionário
      if (t) < (n): #isso aqui testa se já chegamos a última posição
        r2[t+1] = r[t]
      t += 2
  else:
    while t <= (n):   #1  3 <-loop
      r2[t] = r[t]    #12 34! <-valores sendo distribuidos (todos os valores repetem, não tem impar desta vez)
      r2[t+1] = r[t]
      t += 2

  #preparação para a conta final
  f={}
  t=1
  while t <= n:
    f[t] = 1/r2[t]
    t += 1

  #foi necessário usar uma lista...
  fl =[]
  t=1
  while t <= n:
    fl.append(f[t])
    t +=1

  #conta final
  gg = 1 / sum(fl)
  return gg
