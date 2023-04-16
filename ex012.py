p = float(input('Qual o valor do produto? R$'))
novo = p - (p * 5 / 100)
print('O produto que valia R${:.2f} com desconto de 5% fica em R${:.2f}'.format(p, novo))
