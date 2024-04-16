import hashlib
from bit import Key
from bit.format import bytes_to_wif
from get_balance import get_balance_list

#CRIA A LISTA DE KEY_HEX E ADDRESS COMPRESS, UNCOMPRESS E SEGWIT
def set_list_address(palavras,filename_save,value):
    list_address_key = []
    e_list = []
    texto = []
    texto.append(str(palavras))

    if int(value) == 1 or int(value) == 4:
        e_list = texto
    else:
        e_list = palavras  

    for palavra in e_list:       
        key = Key.from_hex(str.strip((hashlib.sha256(str(palavra).encode('utf-8'))).hexdigest()))
        wif_uncompressed = bytes_to_wif(key.to_bytes(), compressed=False)
        wif_compressed = bytes_to_wif(key.to_bytes(), compressed=True)
        key_uncomp = Key(wif_uncompressed)
        key_comp = Key(wif_compressed)
        list_address_key.append(f'{key_uncomp.address}/{key.to_hex()}')
        list_address_key.append(f'{key.address}/{key.to_hex()}')
        list_address_key.append(f'{key.segwit_address}/{key.to_hex()}')
    get_balance_list(list_address_key,filename_save)
