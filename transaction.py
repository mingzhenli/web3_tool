import  argparse
from loguru import logger

from libs.util_tools import exeProcess, printProcess
from model.address import Address
from model.config import Config
from model.send_address import SendAddress
from model.transactions import Transactions
from service.transaciton_service import TransactionsService


class TransactionExec():
    def __init__(self):
        args = parser.parse_args()
        self.feature = args.feature
        self.process = args.process
        self.count = args.count
        match self.feature:
            case "send":
                self.send()
            case "check":
                self.check_tran()
            case 'get_balance':
                self .get_balance()


    def send(self):
        config = Config().get_value_by_key(1)

        address_list = Address().get_list(self.process)
        logger.success(f'count:{self.count}, process:{self.process}')
        keys = config.value['private_key']
        logger.success(address_list)
        transaction_service = TransactionsService(keys)
        for index,item in enumerate(address_list):
            logger.success(index)
            logger.success(item)
            transaction_service.transaction(item, 0.0018,index,self.process)
        logger.success("执行完成")

    def check_tran(self):

        tran_list = Transactions().get_list(1)
        transaction_service = TransactionsService()
        for index, item in enumerate(tran_list):
            logger.success(index)
            logger.success(item)
            logger.success(item.hash)
            logger.success(f"开始查询第{index+1}比交易，id:{item.id}")
            res = transaction_service.check_transaction(item.hash,item.id)
            if res :
                logger.success(f"第{index+1}交易成功，id:{item.id}")
            else:
                logger.success(f"第{index + 1}交易失败，id:{item.id}")
        logger.success('程序执行完成')

    def get_balance(self):
        list = SendAddress().get_balance_list()
        exeProcess['total'] = len(list)
        for item in list:
            balance = TransactionsService().get_get_balance(item.address)
            res=SendAddress().update(item.id,{'balance':balance})
            if res:
                exeProcess['done'] += 1
            else:
                exeProcess['fail']+=1
            printProcess(exeProcess)





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.description = 'Please enter task name , process name , extend params'
    parser.add_argument("-f", help="execute task name", dest="feature", type=str, default="mint")
    parser.add_argument("-p", help="process name", dest="process", type=str, default="mac")
    parser.add_argument("-c", help="count", dest="count", type=int, default="0")

    try:
        TransactionExec()
    except Exception as e:
        logger.error(e)

