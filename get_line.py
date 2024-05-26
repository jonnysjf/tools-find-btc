adr = input('find adr: ')
with open('../list/all_Bitcoin.tsv', 'r', encoding = 'utf-8') as file:
    for i, line in enumerate(file):
        if str.strip(line) == adr:
            print(i)