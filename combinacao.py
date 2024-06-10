import itertools

quantdigitos = int(input('Digite a quantidade digitos :'))
algarismos = str(input('Digite os algarismos separados por virgula :'))

permutacao = itertools.permutations(algarismos, r = quantdigitos)

for number in permutacao:
    print(''.join(number))