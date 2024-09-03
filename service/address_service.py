from eth_utils import to_checksum_address
from mnemonic import Mnemonic
from eth_keys import keys


class AddressService:


    def create_mnomem(self):
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(12) # 生成 24 个单词的助记词
        print(f"助记词: {mnemonic_phrase}")

    def create_account(self):
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=256)
        # 通过助记词生成种子
        seed = mnemo.to_seed(mnemonic)
        # 通过种子生成私钥
        private_key = keys.PrivateKey(seed[:32])
        # 通过私钥生成以太坊地址
        address = to_checksum_address(private_key.public_key.to_checksum_address())

        print(f"助记词: {mnemonic}")
        print(f"私钥: {private_key}")
        print(f"地址: {address}")






if __name__ == '__main__':
    address_service = AddressService()
    address_service.create_account()