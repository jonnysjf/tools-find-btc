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


#MENU DE OPÇÕES
def select(value):
     if value == 1:
          print(es.YELLOW + str.upper('modo good luck! selecionado !') + es.RESET)
          mgl()
     elif value == 2:
          print(str.upper('Sequencia de Data'))
          
     elif value == 3:
          print(str.upper('Sequencia de Palavras'))
          option = int(input("[1] Carregar arquivo \n[2] Digitar textoSair \n: "))
          
     elif value == 4:
          print(str.upper('Imagens'))
          filename = input("Local da imagens : ")
          n_file_save = (f'Resultado_{filename}.tsv')
          
     else:
          print('Nenhuma opção selecionada')
          main()
   
#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def main():
      select(int(input("[1] Good Luck! \n[2] Find Duplicidade \n[3] Extrair Addresses (100.000)\n[4] Compilar fail's excluindo repetidos \n[0] Sair \n: ")))  

if __name__ == '__main__':
	main()