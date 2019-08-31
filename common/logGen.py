import logging
import os
from datetime import datetime


class LogGen:
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        lt = datetime.now().strftime('%Y%m%d%H%M%S')

        log_file = os.path.join(os.path.dirname(os.getcwd()), "logs", lt+'.log')
        # 文件中打印
        fileh = logging.FileHandler(log_file)
        fileh.setLevel(logging.INFO)
        # 终端打印
        consoleh = logging.StreamHandler()
        consoleh.setLevel(logging.INFO)

        # 格式化，固定写法
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)

    def get_log(self):
        return self.logger
