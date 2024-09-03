import time,json,os
from datetime import datetime
from loguru import logger
from urllib.parse import urlparse, parse_qs

exeProcess = {
    'process': '',
    'total': 0,
    'start': 0,
    'average': 0,
    'done': 0,
    'fail': 0,
    'rest': 0,
}

def get_today_sign():
    return datetime.now().strftime('%y%m%d')

def print_process(exeProcess):
    exeProcess['rest'] = exeProcess['total'] - exeProcess['done']
    exeProcess['average'] = (int(time.time()) - exeProcess['start']) / exeProcess['done']
    logger.warning(f"process:{exeProcess['process']}, total:{exeProcess['total']}, done:{exeProcess['done']}, "
                   f"est:{exeProcess['rest']}, fail:{exeProcess['fail']}, average:{round(exeProcess['average'], 3)}s")

def file_get_content(path):
    path = os.path.join(os.path.dirname(__file__), path)
    # 打开文件
    with open(path, 'r') as file:
        # 读取文件全部内容
        content = file.read()
    return content

def read_file(path):
    return open(os.path.join(os.path.dirname(__file__), path), 'r', encoding='utf-8')

def load_abi(path):
    return json.load(read_file("../abi/" + path))

def generate_curl(url, headers, json_body):
    # 转换字典为JSON字符串，用于curl命令的--data参数
    json_data = json.dumps(json_body)
    # 转换headers字典为curl格式的headers
    headers_list = [f"-H '{k}: {v}'" for k, v in headers.items()]
    headers_str = " ".join(headers_list)
    # 组装curl命令
    curl_command = f"curl -X POST {headers_str} --data '{json_data}' '{url}'"
    return curl_command

def get_query_param(url: str, name: str):
    return parse_qs(urlparse(url).query).get(name)[0]

def build_abi_code(methodID=0, params=None):
    data = []
    for num in params:
        hex_str = format(num, 'x') if not isinstance(num, str) else num
        padded_hex_str = str(hex_str).zfill(64).lower()
        # print(padded_hex_str)
        data.append(padded_hex_str)
    hexStr = methodID + '' .join(data)
    # print(hexStr)
    return hexStr

 # 将object转为dict
def object_to_dict(obj):
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

# 将list转为数组dict
def list_to_dicts(objs):
    return [object_to_dict(obj) for obj in objs]

