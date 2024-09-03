
from web3 import Web3

rpc_url = 'http://127.0.0.1:8545'
class TransactionsService:

    def __init__(self, private_key = None):
        self.private_key = private_key
        self.base_web3 = Web3(Web3.HTTPProvider(rpc_url))
