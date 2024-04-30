import hashlib
from bit import Key
from bit.format import bytes_to_wif
from itertools import starmap 
from datetime import datetime, timedelta
import pandas as pd
from set_address import set_list_address
import estilos as es
import os
import glob
from pathlib import Path

SATOSHIS_PER_BTC = 1e+8
list_origem = []

#CRIA SEQUENCIA FIBONACCI DE ACORDO COM NÚMEROS DE DIGITOS INFORMADO
def seq_fibonacci(n_termos,file_save,value):
    num1 = 0
    num2 = 1
    next_number = num2  
    count = 1
    word =''
    
    while count <= int(n_termos):
        #print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
        list_origem.append(next_number)
    for z in list_origem:
         word = word + str(z)
    set_list_address(word,file_save,value)

#CRIA UMA LISTA DE DATAS CONFORME RANGE DEFINIDO
def seq_datas(value):
     list_data = []
     list_data_format = []
     inicio = datetime.strptime(input('Data Inicial :'),'%d/%m/%Y')
     final = datetime.strptime(input('Data final :'),'%d/%m/%Y')
     intervalo = timedelta(days=1)
     data_atual = inicio
     n_file_save = (f'Datas_{str(inicio)[:10]}_{str(final)[:10]}.tsv')

     while data_atual <= final:
        list_data.append(data_atual)
        data_atual += intervalo
     for data in list_data:
        list_data_format.append(str(data)[:10])
     set_list_address(list_data_format,n_file_save,value)

def op_type_text(option,value):
     palavra = []
     if option == 1:
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
          value = 2
          
          with open(f'../list/{file_list}') as file:
               for line in file:
                    addr = str.strip(line)
                    palavra.append(addr)  
     else:
          value = 1
          palavra = str(input('Digite a palavra / texto :'))
          n_file_save = (f'Resultados_word_{palavra}.tsv')

     set_list_address(palavra,n_file_save,value) 

def get_img(file,n_file_save,value):
     with open(file,"rb") as f:
        bytes = f.read()
        set_list_address(bytes,n_file_save,value)    

#MENU DE OPÇÕES
def opt_select(value):
     if value == 1:
          print(str.upper('Sequencia Fibonacci'))
          n_termos = int(input('Quantidade de termos :'))
          n_file_save = (f'Resultado_Fibonacci_{n_termos}.tsv')
          seq_fibonacci(n_termos,n_file_save,value)
     elif value == 2:
          print(str.upper('Sequencia de Data'))
          seq_datas(value)
     elif value == 3:
          print(str.upper('Sequencia de Palavras'))
          op = int(input("[1] Carregar arquivo \n[2] Digitar textoSair \n: "))
          op_type_text(op,value)
     elif value == 4:
          print(str.upper('Get hash de Imagem'))
          filename = input("Local da imagens : ")
          n_file_save = (f'Resultado_{filename}.tsv')
          get_img(filename,n_file_save,value)   
     else:
          print('Nenhuma opção selecionada')
          mainGoodLuck()
#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def mainGoodLuck():
     
      opt_select(int(input("[1] sequência fibonacci \n[2] sequência de datas \n[3] sequência de palavras\n[4] imagens \n[0] Voltar \n: ")))  