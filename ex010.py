real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.16
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
