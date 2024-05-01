import sys
import hashlib
import json
from json.decoder import JSONDecodeError
import requests
from pathlib import Path
import estilos as es
from urllib.request import urlopen


SATOSHIS_PER_BTC = 1e+8

list = '1400001_1500000.tsv'

txt = '''{
  "tx_hash": "9ec4bc49e828d924af1d1029cacf709431abbde46d59554b62bc270e3b29c4b1",
  "block_height": 170399,
  "confirmed": 671294,
  "fees": 50000,
  "size": 402,
  "received_date": "2015-04-06T11:06:57.713",
  "version": 1,
  "lock_time": 0,
  "inputs": [
    {
      "prev_hash": "01f7ba55e5baac3d9cbc38722b19c07cb0cd2d2b25f4c270af4d9f2f3e604cf6",
      "prev_index": 1,
      "value": 130000,
      "script": "primeiro",
      "address": "1BFhrfTTZP3Nw4BNy4eX4KFLsn9ZeijcMm",
      "sequence": 4294967295
    },
    {
      "prev_hash": "4a85d9c86ba415f489be1ec68f67e862e9c3d8d13c892a3afacaa02bdb41f829",
      "prev_index": 1,
      "value": 20000,
      "script": "segundo",
      "address": "1BFhrfTTZP3Nw4BNy4eX4KFLsn9ZeijcMm",
      "sequence": 4294967295
    }
  ],
  "outputs": [
    {
      "value": 100000,
      "script": "76a91470792fb74a5df745bac07df6fe020f871cbb293b88ac",
      "address": "1BFhrfTTZP3Nw4BNy4eX4KFLsn9ZeijcMm"
    }
  ]
}'''

def get_rsz(list,pvt,fail,begin):
    url = 'https://chainflyer.bitflyer.jp/v1/tx/'
    linha = 0
    soma_balance = 0
    total_encontrado = 0
    with open(f'../list/{list}') as file:
        for line in file:
            result_pvt = open(f'../list/{pvt}', 'a')
            linha = linha + 1
            line_cache = linha
            if linha >= int(begin): 
                address = str.strip(line)
                tx = '9ec4bc49e828d924af1d1029cacf709431abbde46d59554b62bc270e3b29c4b1'
                url_tx = url + tx
                #response = urlopen(url_tx)

                j_line = json.loads(txt)
                j_inputs = j_line['inputs']
            
                for x in j_inputs:  
                    print(x['script'])


                #if (response.status_code != 204 and response.headers["content-type"].strip().startswith("application/json")):
                        #saldo = (float(j_line['confirmed_balance']))/SATOSHIS_PER_BTC
                        



def novo():
    mypath = '../list/'
    list_file = Path(mypath).glob("*.tsv")
    list_file = sorted(list_file)
    for i, file in enumerate(list_file):
        print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

    indice = int(input("\nDigite o número referente ao aqruivo: "))
    file_list = list_file[indice].name
    inicio = 1
    file_pvtkey = (f'pvtkey_No_Zero_{file_list}')
    file_fail = (f'fail_{file_list}')
    print(f'File Select - {file_list} / Linha inicial {inicio}')
    get_rsz(file_list,file_pvtkey,file_fail,inicio)

def continuar():
    mypath = '../list/'
    list_file = Path(mypath).glob("*.tsv")
    list_file = sorted(list_file)
    for i, file in enumerate(list_file):
        print(f'[{i}]\t{es.CYAN}{file.name}{es.RESET}')

    indice = int(input("\nDigite o número referente ao aqruivo: "))
    file_list = str(list_file[indice].name)
    file_pvtkey = (f'pvtkey_No_Zero_{file_list}')
    file_fail = (f'fail_{file_list}')
    with open(f'../list/{file_pvtkey}') as f:
        inicio = len(f.readlines())
        print(inicio)
    print(file_list)
    print(f'File Select - {file_list} / Linha inicial {inicio}')
    get_rsz(file_list,file_pvtkey,file_fail,inicio)

def mainNoZero():
      select = int(input("[1] Novo  \n[2] Continuar \n[0] Sair \n: "))
      novo() if select == 1 else continuar()

if __name__ == '__main__':
	mainNoZero()