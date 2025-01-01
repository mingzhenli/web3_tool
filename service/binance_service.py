
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
        amount = 0.00084  # 提币数量
        # address = "your_wallet_address"  # 提币地址
        network = "ARBITRUM"  # 提币网络，如 BTC、BSC
        address_tag = None  # 标签（如 XRP、XMR 等需要标签）
        try:
            result = self.binance_client.withdraw(
                coin=asset,
                address=address,
                amount=amount,
                network=network,
                addressTag=address_tag
            )
        except BinanceAPIException as e:
            print("Binance API Exception:", e)
        except BinanceRequestException as e:
            print("Binance Request Exception:", e)
        except Exception as e:
            print("Exception:", e)



if __name__ == '__main__':
    res = BinanceService()
    res.with_draw()