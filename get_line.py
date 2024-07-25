import estilos as es
from pathlib import Path

adr = input('find addr/text: ')
mypath = '../list/'
list_file = Path(mypath).glob("*.tsv")
list_file = sorted(list_file)

for i, file in enumerate(list_file):
    print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

indice = int(input("\nDigite o número referente ao aqruivo: "))
file_list = (f'../list/{list_file[indice].name}')
print(f'Busca realizada no arquivo : {list_file[indice].name}')


with open(file_list, 'r', encoding = 'utf-8') as file:
    for i, line in enumerate(file):
        #print(line[0])
        if line[0] == str.upper(adr):
            print(f'{i} - {str.strip(line)}')