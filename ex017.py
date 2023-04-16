from math import hypot
co = float(input('Qual o valor do cateto oposto: '))
ca = float(input('Qual o valor do cateto adjacente: '))
print('Se o cateto oposto é {} e o cateto adjacente é {} a hipotenusa é {:.2f}'.format(co, ca, hypot(co, ca)))
