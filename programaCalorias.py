print(('-' * 10), 'QUANTAS CALORIAS EU DEVO INGERIR POR DIA', ('-' * 10))

print('Eu desejo saber o quanto eu devo ingerir para...'
      '\n 1 - Emagrecer'
      '\n 2 - Manter o peso'
      '\n 3 - Para engordar')
resposta = int(input('RESPOSTA: '))

peso = float(input('Digite o seu peso: '))

if resposta == 1:
    emagrecer = peso * 20
    print('Você precisa ingerir {} kalorias por dia para emagrecer'.format(emagrecer))
elif resposta == 2:
    manter_peso = peso * 30
    print('Você precisa ingerir {} kalorias por dia para manter o peso'.format(manter_peso))
else:
    engordar = peso * 35
    print('Você precisa ingerir {} kalorias por dia para engordar'.format(engordar))
