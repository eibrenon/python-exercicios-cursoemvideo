from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))
print('O seno de {} é {:.2f}'.format(angulo, sin(radians(angulo))))
print('O cosseno de {} é {:.2f}'.format(angulo, cos(radians(angulo))))
print('A tangente de {} é {:.2f}'.format(angulo, tan(radians(angulo))))
