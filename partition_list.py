
def read_file(file_read,first,end,file_save):
    print(f'read file: {str.strip(file_read)} / range: {first} to {end} / save file: {file_save}')

    with open(file_read) as file:
        linha = 0

        for line in file:
            file_saved = open(file_save,'a')  
            linha = linha + 1
            
            if linha <= int(end):            
                if ((linha >= int(first)) and (linha <= int(end))):
                    print(f'{linha} - {str.strip(line)}')
                    file_saved.write(f'{str.strip(line)}\n')
            else:
                break

            file_saved.close()
                
                #check_balance(address,file_balance)

def info_partition():
      file_list = input("Entre com endereço do file_list :  ")
      inicio = input("Entre com linha inicial :  ")
      final = input("Entre com linha final :  ")
      file_result = (f'../list/{inicio}_{final}.tsv')
      print(file_list)
      read_file(file_list,inicio,final,file_result)