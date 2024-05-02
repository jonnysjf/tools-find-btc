import requests
from pathlib import Path
import estilos as es
import json

SATOSHIS_PER_BTC = 1e+8

mypath = '../list/'
list_file = Path(mypath).glob("*.tsv")
list_file = sorted(list_file)

for i, file in enumerate(list_file):
    print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

indice = int(input("\nDigite o número referente ao aqruivo: "))
file_list = list_file[indice].name
print(file_list)
n_file_save = (f'Resultado_{file_list}.tsv')
print(n_file_save)

with open(f'../list/{file_list}') as file:
        for line in file:
            address = str.strip(line)
            response = requests.get('https://chainflyer.bitflyer.jp/v1/address/' + address)
            response.raise_for_status()
            result_pvt = open(f'../list/{n_file_save}', 'a')
            if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                j_line = json.loads(response.text)
                saldo = (float(j_line['confirmed_balance']))/SATOSHIS_PER_BTC
                if saldo > 0.0:
                    print(f'{address} - {saldo}')
                    result_pvt.write(f'{address} - {saldo}\n')
                    print('-'*120)