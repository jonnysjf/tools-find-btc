import math
from typing import final

range_66_inicio = '20000000000000000'
range_66_final = '3ffffffffffffffff'


def getRange():
    select = input('Puzzle 66, y/n? ')
    if select == 'y':
        va_int_ini = int(range_66_inicio,16)
        va_int_final = int(range_66_final,16)
    else:
        va_int_ini = int(input('Digite o hex inicial: '),16)
        va_int_final = int(input('Digite o hex final: '),16)
    
    range_int = va_int_final - va_int_ini
    percentual = float(input('Digite o inicio % desejada do range: '))
    range = int(input('Digite o tamanho desejado do range: '))
    inicio = va_int_ini + int(range_int * percentual)
    final = inicio + range
    print(f'inicio decimal {inicio}')
    print(f'fim decimal {final}')
    print(f'inicio hex {hex(inicio)[2:]}')
    print(f'fim hex {hex(final)[2:]}')