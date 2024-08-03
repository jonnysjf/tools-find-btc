import requests
import json
from json.decoder import JSONDecodeError
import estilos as es
import xmltodict
from pathlib import Path

SATOSHIS_PER_BTC = 1e+8
addr = []
token = 12345678901234567890123456789012
#CHECA O SALDO DE ACORDO COM A LISTA DE ENDEREÇOS CRIADAS
def get_balance_list(file_list):
    found = 0
    found_line = 0
    file_list = str(f'../list/{file_list}')
    print(file_list)
    filename_save = str(f'../list/fsave.tsv')
    with open(filename_save,'a') as f_save:
        for line in file_list:
            addr = line.strip('\n')
            print(addr)
            print(line)
            response=requests.get('https://chainflyer.bitflyer.jp/v1/address/' + str.strip(addr))
            #response=requests.get(f'https://coinb.in/api/?uid=1&key={token}&setmodule=addresses&request=bal&address={str.strip(addr)}')
            #j_line = json.loads(json.dumps(xmltodict.parse(response.content), indent=4))
            response.raise_for_status()
            if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                try:
                    j_line = json.loads(response.text)
                    saldo = (j_line['request']['balance'])/SATOSHIS_PER_BTC
                    print(f'{es.CYAN + addr + es.RESET} {es.GREEN + str(saldo) + es.RESET} Found :{found} Lines :{found_line}')
                    #verificar a saida dos hex para poder salvar no arquivo
                    if saldo >= 0.0001:
                        f_save.write(f'{addr}/{saldo}\n')
                        found = found + 1
                        found_line = (f'{found_line},')
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


            