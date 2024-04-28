import requests
import json
from json.decoder import JSONDecodeError
import estilos as es

SATOSHIS_PER_BTC = 1e+8
addr = []

#CHECA O SALDO DE ACORDO COM A LISTA DE ENDEREÇOS CRIADAS
def get_balance_list(list_address,filename_save):
    found = 0
    found_line = 0
    print(filename_save)
    with open(filename_save,'a') as f_save:
        for i,line in enumerate(list_address):
            separador = line.split('/')
            addr = separador[0]
            hex = separador[1]
            response=requests.get('https://chainflyer.bitflyer.jp/v1/address/' + str.strip(addr))
            response.raise_for_status()
            if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                try:
                    j_line = json.loads(response.text)
                    saldo = (j_line['confirmed_balance'])/SATOSHIS_PER_BTC
                    print(f'{i} - {es.CYAN + addr + es.RESET} {es.GREEN + str(saldo) + es.RESET} {es.YELLOW + hex + es.RESET} Found :{found} Lines :{found_line}')
                    #verificar a saida dos hex para poder salvar no arquivo
                    if saldo >= 0.0001:
                        f_save.write(f'{i} - {addr}/{saldo}/{hex}\n')
                        found = found + 1
                        found_line = (f'{found_line}, {i}')
                    else:
                        pass
                except JSONDecodeError as e:
                    pass
