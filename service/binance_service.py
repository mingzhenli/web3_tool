
from binance import Client
from loguru import logger

from model.config import Config


class BinanceService:
    def __init__(self):
        binance_config = Config().get_value_by_key(2).value
        api_key =  binance_config['api_key']
        secret_key= binance_config['secret_key']
        self.binance_client = Client(api_key,secret_key)
        logger.info(api_key)



    def with_draw(self,to_address = None):
        asset = 'ETH'
        balance = self.binance_client.get_asset_balance(asset = asset)
        logger.success(f'balance:{balance}')



if __name__ == '__main__':
    res = BinanceService()
    res.with_draw()