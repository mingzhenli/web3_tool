import json
from inspect import signature

from conda.common.serialize import json_dump
from eth_account.messages import encode_defunct
from loguru import logger
import requests
from web3 import Web3

rpc_url = 'https://mainnet.infura.io/v3/'
chain_id = 1
private_key = '0x610384827e1c303df7f0d9777c92c44766e2b3662bc993a783b36f76e96fe41a'
wb3 = Web3(Web3.HTTPProvider(rpc_url))
# account = wb3.eth.account.from_key(private_key)
messages = "Welcome to MOONGATE!\n\nBy signing, you accept the MOONGATE Terms of Service:\nhttps://themoongate.notion.site/Moongate-Terms-and-Conditions-3f98c36fff344ba2811a7bc17b5d2056\nand Privacy Policy:\nhttps://themoongate.notion.site/Moongate-Privacy-f4f35ff31d98430680b5453441dc3d18\n\nThis request will not trigger a blockchain transaction or cost any gas fees.\n\n"

messages_encode = encode_defunct(text=messages)
signed_message = wb3.eth.account.sign_message(messages_encode, private_key=private_key)
signature = signed_message.signature.hex()#
# # 打印签名
print(f'Signature: {signed_message.signature.hex()}')
print(f'Message hash: {signed_message.messageHash.hex()}')





#
#
url = "https://api.moongate.id/users/f7d4fa2d-ac66-4895-a4e8-97690b4bb045/wallets"
payload = json.dumps({
   "network": "evm",
   "address": "0x1580b682a4f5b17ae05e771a9dc462f35b90a5b8",
   "siweMessage": {
      "domain": "app.moongate.id",
      "address": "0x1580b682A4f5B17Ae05E771a9Dc462f35B90a5B8",
      "statement": "Welcome to MOONGATE!\n\nBy signing, you accept the MOONGATE Terms of Service:\nhttps://themoongate.notion.site/Moongate-Terms-and-Conditions-3f98c36fff344ba2811a7bc17b5d2056\nand Privacy Policy:\nhttps://themoongate.notion.site/Moongate-Privacy-f4f35ff31d98430680b5453441dc3d18\n\nThis request will not trigger a blockchain transaction or cost any gas fees.\n\n",
      "uri": "https://app.moongate.id",
      "version": "1",
      "chainId": 1,
      "nonce": "75650400",
      "issuedAt": "2024-09-05T01:40:00.187Z"
   },
   "signature": signature
})
headers = {
   'authorization': 'Bearer 6c08b5e178e7a9fdfd3ca19afbfa5316',
   'priority': 'u=1, i',
   'Cookie':'_ga=GA1.1.1405678008.1725459848; moongate-auth-id-240710=f7d4fa2d-ac66-4895-a4e8-97690b4bb045; _ga_G8FBZD736N=GS1.1.1725499899.3.1.1725500050.0.0.0; moongate-auth-token-240710=eyJhbGciOiJSUzI1NiJ9.eyJ1aWQiOiJmN2Q0ZmEyZC1hYzY2LTQ4OTUtYTRlOC05NzY5MGI0YmIwNDUiLCJlbWFpbCI6ImFmYzkzY2UxMWYyZDRmN2NkNTA1OWU1YzQ3NWM1NjY2OGFmM2MyYTcxNjViZDIwMWMyOGY4ZjQ2NmM2NmViZmYiLCJzZXNzaW9uIjoiYmY2OGU1OTg5YTAwNWU2ZjYxOGZkYjI0NDhhODk4NjM2MzFiN2U2MjY3ZGJiMjIwOTBiMDJiZDM2YWExMzBiMGFhY2YzMzhmYWJlNmI5ZmM2OTY0ZTQ0OTRhZDczNmZiZDcwZWE4ODg0OWQyYTMyNWQ5OGZmMGNjOWZlNTNjZTMwNzdiN2JlMmFkNjViZDIyM2Q2NDdhOTRhZTAxMTAwOCIsImlhdCI6MTcyNTUwMDA1NCwiZXhwIjoxNzI2MTA0ODU0LCJpc3MiOiJtb29uZ2F0ZS5pZCIsImF1ZCI6Im1vb25nYXRlLmlkIiwic3ViIjoiZjdkNGZhMmQtYWM2Ni00ODk1LWE0ZTgtOTc2OTBiNGJiMDQ1In0.frEY-hszOpKRmJ3hxEmk4IMKzvsG8mnw7cekKPNbTAq_fzl_JtRj0h6hAyyy8rt8BdDBvlZqTJtPPNtmsXHcA_1m-FThMfpSTlgrAP9F4YeQa3CFwf2qwbNSyihkpcMUg59PTDhWHX03vPVdtvEfrTZmsWxB3cbNkVXyBS3N1dtMiBoAEJXeh2EMZ93Ba72juUYkJOqA-pPqSRj76vKAXirqXCr6VVq35ePMh66xOwzFTz3IVTFYXMIKVvtqQBavsmdLwsr_TCZg67_eNryDJFAkZM_m5tPkFRxD1b82zo5Su6gA7U3RZPcU6C-4REzsLQZlgLOpnUh6DYGSjx8Jvg',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
   'if-none-match':'W/"6c28-3rLZv6+2Ix0BpunWxPwOHBqCpdE"',
   'content-type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

