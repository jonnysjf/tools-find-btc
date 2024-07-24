#Estilo definições via Colorama
import estilos as es 
#Importações de modulos/Calsses
from good_luck import mainGoodLuck as mgl
from partition_list import info_partition
from chk_duplo_r_nozero import mainNoZero as mnz
from chk_duplo_all import mainAll as mna
from puzzle_range import getRange
import estilos as es


#Menu de Opções Iniciais, com as ferramentas disponiveis
def select(value):
     if value == 1:
          print(es.YELLOW + str.upper('good luck!') + es.RESET)
          mgl()
     elif value == 2:
          print(es.GREEN + str.upper('Find assinaturas fracas') + es.RESET)
          op_type = int(input("[1] Address com balance  \n[2] All address \n[0] Sair \n: "))
          mnz() if op_type == 1 else mna()
     elif value == 3:
          print(es.BLUE + str.upper('Dividir Arquivo master em arquivos de 100.000 address ') + es.RESET)
          info_partition()
     elif value == 5:
          print(es.BLUE + str.upper('get range puzzle chalenger ') + es.RESET)
          getRange()
     elif value == 6:
          print(es.BLUE + str.upper('check balance from list address ') + es.RESET)
          getRange()
     else:
          print('Nenhuma opção selecionada')
          main()
   
#APRESENTAÇÃO DO MENU PARA ESCOLHA     
def main():
     select(int(input("[1] Good Luck! \n[2] Find Assinaturas fracas \n[3] Segregar List (100.000 addresses)\n[4] Compilar fail's excluindo repetidos \n[5] Get range for puzzle \n[6] Check balance from file \n[0] Sair \n: ")))  

if __name__ == '__main__':
	main()