from bitcoinlib.wallets import Wallet, wallet_create_or_open
from bitcoinlib.keys import HDKey

# Cria uma nova carteira com um nome específico
wallet_name = 'MyBitcoinWallet'
password = 'my_secure_password'

# Cria uma nova carteira
wallet = wallet_create_or_open(wallet_name, password=password)

# Gera uma nova chave mestra (HDKey)
master_key = HDKey().wif()

# Adiciona a chave mestra à carteira
wallet.new_key(name='Master Key')

# Salva a carteira
#wallet.save()

print(f"Carteira criada com sucesso: {wallet_name}")
print(f"Endereço da carteira: {wallet.get_key().address()}")