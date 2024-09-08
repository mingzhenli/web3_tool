import  argparse
from loguru import logger

from service.address_service import AddressService



class AdddressExec():
    def __init__(self):
        args = parser.parse_args()
        self.feature = args.feature
        self.process = args.process
        self.count = args.count
        match self.feature:
            case "create":
                self.create()


    def create(self):
        logger.success(f'count:{self.count}, process:{self.process}')
        for i in range(self.count):
            address_service = AddressService()
            address_service.create_account(self.process)
        logger.success("执行完成")





if __name__ == '__main__':
    # for i in range(20):
    #     address_service = AddressService()
    #     address_service.create_account('test')
    # logger.success("执行完成")

    parser = argparse.ArgumentParser()
    parser.description = 'Please enter task name , process name , extend params'
    parser.add_argument("-f", help="execute task name", dest="feature", type=str, default="mint")
    parser.add_argument("-p", help="process name", dest="process", type=str, default="mac")
    parser.add_argument("-c", help="count", dest="count", type=int, default="0")

    try:
        AdddressExec()
    except Exception as e:
        logger.error(e)

