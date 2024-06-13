import requests
import json
from json.decoder import JSONDecodeError
import estilos as es

from pathlib import Path

SATOSHIS_PER_BTC = 1e+8
addr = []

#CHECA O SALDO DE ACORDO COM A LISTA DE ENDEREÇOS CRIADAS
def get_balance_list(file_list):
    found = 0
    found_line = 0
    filename_save = str(f'../list/fsave_{file_list}')
    with open(filename_save,'a') as f_save:
        for i,line in enumerate(file_list):
            addr = line
            print(addr)
            response=requests.get('https://chainflyer.bitflyer.jp/v1/address/' + str.strip(addr))
            response.raise_for_status()
            if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                try:
                    j_line = json.loads(response.text)
                    saldo = (j_line['confirmed_balance'])/SATOSHIS_PER_BTC
                    print(f'{i} - {es.CYAN + addr + es.RESET} {es.GREEN + str(saldo) + es.RESET} Found :{found} Lines :{found_line}')
                    #verificar a saida dos hex para poder salvar no arquivo
                    if saldo >= 0.0001:
                        f_save.write(f'{i} - {addr}/{saldo}\n')
                        found = found + 1
                        found_line = (f'{found_line}, {i}')
                    else:
                        pass
                except JSONDecodeError as e:
                    pass


#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def main():
    mypath = '../list/'
    list_file = Path(mypath).glob("*.tsv")
    list_file = sorted(list_file)

    for i, file in enumerate(list_file):
        print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

    indice = int(input("\nDigite o número referente ao aqruivo: "))
    file_list = list_file[indice].name
    print(file_list)
    get_balance_list(file_list)


if __name__ == '__main__':
	main()


            