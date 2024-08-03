import xmltodict
import requests
import json
token = 12345678901234567890123456789012

addr = '12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX'

response=requests.get(f'https://coinb.in/api/?uid=1&key={token}&setmodule=addresses&request=bal&address={str.strip(addr)}')
j_line = json.loads(json.dumps(xmltodict.parse(response.content), indent=4))
#j_line = json.loads(response.text)
saldo = (j_line['request']['balance'])

print(saldo)

