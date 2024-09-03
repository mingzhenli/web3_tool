from loguru import logger

from model import Accounts
info = Accounts().get_user_info(1500)
logger.success(info.id)