import requests

def get_transaction_outputs(txid):
    url = f'https://blockchain.info/rawtx/{txid}'
    response = requests.get(url)
    if response.status_code == 200:
        transaction = response.json()
        outputs = transaction.get('out', [])

        addresses = []
        for output in outputs:
            if 'addr' in output:
                addresses.append(output['addr'])

        return addresses
    else:
        print(f"Failed to fetch transaction {txid}. Status code: {response.status_code}")
        return []

# Exemplo de uso
if __name__ == "__main__":
    transaction_id = str(input('insira o TX : '))  # Substitua pelo ID da transação desejada
    addresses = get_transaction_outputs(transaction_id)
    print("Endereços de saída da transação:")
    for address in addresses:
        print(address)
