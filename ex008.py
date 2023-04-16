n = float(input('Digite uma distância em metros: '))
dm = n * 10
cm = n * 100
mm = n * 1000
dam = n / 10
hm = n / 100
km = n / 1000
print('A medida de {:.1f}m corresponde a: \n'
      '{}km \n{}hm \n{}dam\n{}dm \n{}m \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, km, hm, dam, dm, n, dm, cm, mm))
