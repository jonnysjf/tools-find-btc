import hashlib
from bit import Key
from bit.format import bytes_to_wif
import requests
import json
from itertools import starmap 
from datetime import datetime, timedelta
import pandas as pd
from set_address import set_list_address
from runner_tools import option
   
#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def main():
      option(int(input("[1] Good Luck! \n[2] Find Duplicidade \n[3] Extrair Addresses (100.000)\n[4] Compilar fail's excluindo repetidos \n[0] Sair \n: ")))  

if __name__ == '__main__':
	main()