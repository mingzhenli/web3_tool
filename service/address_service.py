
from eth_utils import to_checksum_address
from loguru import logger
from mnemonic import Mnemonic
from eth_keys import keys
from eth_account import Account

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

    def create_one_mnomem(self):
        # 设置 Web3 自动启用 HD 钱包支持
        Account.enable_unaudited_hdwallet_features()

        # 1. 生成助记词或使用现有助记词
        mnemo = Mnemonic("english")
        # mnemonic_phrase = mnemo.generate(strength=128)  # 生成12个助记词单词
        mnemonic_phrase = "spoon grocery injury feed riot movie fruit impulse debris foster play ranch"  # 替换为已有助记词
        print("助记词:", mnemonic_phrase)

        # 2. 生成根种子
        seed = mnemo.to_seed(mnemonic_phrase)
        self.generate_wallets(mnemonic_phrase,5)

        # 3. 生成多个钱包私钥和地址
    def generate_wallets(self,mnemonic, num_wallets):
        wallets = []
        for i in range(num_wallets):
            # BIP-44 Derivation Path: m/44'/60'/0'/0/i (i 是地址索引)
            path = f"m/44'/60'/0'/0/{i}"
            account = Account.from_mnemonic(mnemonic, account_path=path)
            wallets.append({
                "index": i,
                "address": account.address,
                "private_key": account.key.hex(),
            })

        print(wallets)
        return wallets


    # 4. 找回私钥
    def find_private_key(mnemonic, index):
        path = f"m/44'/60'/0'/0/{index}"
        account = Account.from_mnemonic(mnemonic, account_path=path)
        return account.key.hex()

        # 示例：找回第2个钱包的私钥
        wallet_index = 2
        recovered_private_key = find_private_key(mnemonic_phrase, wallet_index)
        print(f"找回的第{wallet_index}个钱包私钥:", recovered_private_key)






if __name__ == '__main__':
    count = 2
    addressService = AddressService()

    addressService.create_one_mnomem()
