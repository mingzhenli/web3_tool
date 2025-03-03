
from binance import Client, BinanceAPIException, BinanceRequestException
from loguru import logger

from model.config import Config


class BinanceService:
    def __init__(self):
        binance_config = Config().get_value_by_key(2).value
        api_key =  binance_config['api_key']
        secret_key= binance_config['secret_key']
        self.binance_client = Client(api_key,secret_key)
        logger.info(api_key)



    def belance(self):
        asset = 'ETH'
        balance = self.binance_client.get_asset_balance(asset = asset)
        logger.success(f'balance:{balance}')

    def with_draw(self,address):
        # 提币参数
        asset = 'ETH'  # 币种，如 BTC、ETH
        amount = 0.001  # 提币数量
        # address = "your_wallet_address"  # 提币地址
        network = "Optimism"  # 提币网络，如 BTC、BSC
        address_tag = None  # 标签（如 XRP、XMR 等需要标签）
        try:
            result = self.binance_client.withdraw(
                coin=asset,
                address=address,
                amount=amount,
                network=network,
                addressTag=address_tag
            )
            logger.info(result)
            if result and 'id' in result:
                logger.success(result['id'])
                return result['id']
            else:
                return False
        except BinanceAPIException as e:

            logger.error(f'Binance API Exception: {e}')
            return False
        except BinanceRequestException as e:
            logger.error(f'Binance Request Exception: {e}')
            return False
        except Exception as e:
            logger.error(f'Exception: {e}')
            return False



if __name__ == '__main__':
    res = BinanceService()
    res.with_draw()