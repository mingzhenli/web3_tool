from time import sleep

import web3.eth
from loguru import logger
from sqlalchemy import false
from toolz.functoolz import return_none
from web3 import Web3

from libs.util_tools import load_abi, object_to_dict, list_to_dicts
from model.address import Address
from model.config import Config
from model.transactions import Transactions

rpc_url = 'https://ethereum-sepolia.rpc.subquery.network/public'
chain_id = 11155111
class TransactionsService:

    def __init__(self, private_key = None):
        self.private_key = private_key
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        if private_key :
            self.account = self.w3.eth.account.from_key(self.private_key)
            self.nonce = self.w3.eth.get_transaction_count(self.account.address)
            logger.success(self.account.address)


    def transaction(self, item, amount, index, process = 'test'):
        if self.w3.is_connected() is False:
            logger.warning('connected error')
            return False
        logger.warning(f"id:{item.id}")
        nonce = self.nonce + index
        logger.success(f"nonce:{nonce}")
        balance  = self.w3.eth.get_balance(self.account.address)
        gas_price  = self.w3.eth.gas_price
        tx = {
            'nonce': nonce,
            'to': item.address,
            'value': self.w3.to_wei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': self.w3.eth.gas_price,
            'chainId': chain_id
        }
        signed_txn = self.w3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        logger.success(f"tx_hash: {tx_hash.hex()}")
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt :
            Transactions().create({
                "address_id":item.id,
                "amount":amount,
                "hash":tx_hash.hex(),
                "process": process,
                "status": 1
            })
        else:
            Transactions().create({
                "address_id": item.id,
                "amount": amount,
                "hash": tx_hash.hex(),
                "process": process,
                "status": 0
            })
    def check_transaction(self, hash,id):
        receipt = self.w3.eth.get_transaction_receipt(hash)
        try:
            if receipt and receipt['status'] == 1:
                Transactions().update_status(id=id, status=2)
                return receipt
        except Exception as e:
            logger.error(e)




if __name__ == '__main__':
    # address = Address().get_list()
    # logger.success(address)
    # config = Config().get_value_by_key(1)
    # value = config.value
    # private_key = value['private_key']
    # transaction_service = TransactionsService(private_key)
    # for index,item in enumerate(address):
    #     transaction_service.transaction(item, 0.000000001,index)
    transactions = Transactions().get_list(1)
    for item in transactions:
        transaction_service = TransactionsService().check_transaction(item['hash'],item['id'])
    logger.success('全部完成')

    # transaction_service = TransactionsService().check_transaction('0x970d6c11b09b75d24ae1dcf3e688bd4565e6a04aa7af8faec65406186165ed12')
    # logger.success(transaction_service)

