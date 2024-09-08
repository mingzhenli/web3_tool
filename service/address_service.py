
from eth_utils import to_checksum_address
from loguru import logger
from mnemonic import Mnemonic
from eth_keys import keys

from model.address import Address


class AddressService:


    def create_mnomem(self):
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(12) # 生成 24 个单词的助记词
        print(f"助记词: {mnemonic_phrase}")

    def create_account(self, project):
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=256)
        # 通过助记词生成种子
        seed = mnemo.to_seed(mnemonic)
        # 通过种子生成私钥
        private_key = keys.PrivateKey(seed[:32])
        # 通过私钥生成以太坊地址
        address = to_checksum_address(private_key.public_key.to_checksum_address())
        logger.success(f"助记词: {mnemonic}")
        logger.success(f"私钥: {private_key}")
        logger.success(f"地址: {address}")
        res = Address().add_address(address, mnemonic, private_key, project)
        logger.success(res.id)






if __name__ == '__main__':
    count = 2
    addressService = AddressService()
    for i in range(count):
        addressService.create_account()
