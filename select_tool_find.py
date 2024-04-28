import hashlib
from bit import Key
from bit.format import bytes_to_wif
import requests
import json
from itertools import starmap 
from datetime import datetime, timedelta
import pandas as pd
from set_address import set_list_address
from good_luck import mainGoodLuck as mgl
import estilos as es
from partition_list import info_partition
from chk_duplo_r_nozero import mainNoZero as mnz
from chk_duplo_all import mainAll as mna

#MENU DE OPÇÕES
def select(value):
     if value == 1:
          print(es.YELLOW + str.upper('modo good luck! selecionado !') + es.RESET)
          mgl()
     elif value == 2:
          print(es.GREEN + str.upper('Find Assinaturas fracas') + es.RESET)
          op_type = int(input("[1] Address com balance  \n[2] All address \n[0] Sair \n: "))
          mnz() if op_type == 1 else mna()

     elif value == 3:
          print(es.BLUE + str.upper('Particionar lista ') + es.RESET)
          info_partition()
          
     elif value == 4:
          print(str.upper('Imagens'))
          filename = input("Local da imagens : ")
          n_file_save = (f'Resultado_{filename}.tsv')
          
     else:
          print('Nenhuma opção selecionada')
          main()
   
#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def main():
      select(int(input("[1] Good Luck! \n[2] Find Assinaturas fracas \n[3] Segregar List (100.000 addresses)\n[4] Compilar fail's excluindo repetidos \n[0] Sair \n: ")))  

if __name__ == '__main__':
	main()