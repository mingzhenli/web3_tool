import  argparse
import json
from time import sleep
import datetime, time, sys

from eth_utils.network import networks
from loguru import logger


from model.send_address import SendAddress
from service.address_service import AddressService
from service.binance_service import BinanceService
from libs.util_tools import exeProcess, printProcess

class BinanceExec():
    def __init__(self):
        exeProcess['start'] = int(time.time())
        args = parser.parse_args()
        self.feature = args.feature
        self.process = args.process
        self.count = args.count
        self.start_id = args.sid
        self.end_id = args.eid
        match self.feature:
            case "withDraw":
                self.with_draw()
            case 'network':
                self.network()

    def network(self):
        networks = BinanceService().get_network()
        logger.info(json.dumps(networks))

    def with_draw(self):

        send_model = SendAddress()
        list = send_model.get_send_list(self.start_id,self.end_id)
        biance_service = BinanceService()
        exeProcess['total'] = len(list)

        for item in list:
            logger.success(item.address)
            biance_service.belance()
            hash = biance_service.with_draw(item.address)
            logger.info(f'hash:{hash}')
            if id:
                send_model.update(item.id,{'status':1,'hash':hash})
                exeProcess['done'] += 1
            else:
                exeProcess['fail'] += 1
            printProcess(exeProcess)
            sleep(2)








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
    parser.add_argument("-sid", help="start id", dest="sid", type=int, default=1)
    parser.add_argument("-eid", help="end id", dest="eid", type=int, default=200)

    try:
        BinanceExec()
    except Exception as e:
        logger.error(e)

