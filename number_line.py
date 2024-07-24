from pathlib import Path
import estilos as es

mypath = '../list/'
list_file = Path(mypath).glob("*.tsv")
list_file = sorted(list_file)
for i, file in enumerate(list_file):
    print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

indice = int(input("\nDigite o número referente ao aqruivo: "))
file_list = list_file[indice].name
print(file_list)

with open(f'../list/{file_list}') as file:
    lines = len(file.readlines())

print('Total Number of lines:', lines)