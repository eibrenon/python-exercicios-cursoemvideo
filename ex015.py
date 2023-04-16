d = int(input('Digite a quantidade de dias que você usou o carro: '))
km = float(input('Digite a quabtidade de km rodados: '))
vf = (d * 60) + (km * 0.15)
print('Você devera pagar R${:.2f} pelo aluguel do carro!'.format(vf))
