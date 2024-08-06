import hashlib
from bit import Key
from bit.format import bytes_to_wif
import requests
import json
from json.decoder import JSONDecodeError
import estilos as es
from get_balance import get_balance_list

SATOSHIS_PER_BTC = 1e+8
list_address_key = []
filename_save = str(f'../list/fspvtcompress.tsv')
file_list = str(f'../list/pvtuncompress.tsv')

with open(file_list) as f:
        for line in f:
            k_c = line.strip('\n')
            try:
                key_comp = Key(str(k_c))
                response=requests.get('https://chainflyer.bitflyer.jp/v1/address/' + str(key_comp.segwit_address))
                response.raise_for_status()
                if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                    try:
                        j_line = json.loads(response.text)
                        saldo = (float(j_line['confirmed_balance']))/SATOSHIS_PER_BTC
                        print(f'{es.CYAN + key_comp.address + es.RESET} {es.GREEN + str(saldo) + es.RESET}')
                        #verificar a saida dos hex para poder salvar no arquivo
                        if saldo >= 0.0001:
                            filename_save.write(f'{key_comp.address}/{saldo}\n')
                            found = found + 1
                            found_line = (f'{found_line},')
                        else:
                            pass
                    except JSONDecodeError as e:
                                pass
            except ValueError as ex:
                    pass