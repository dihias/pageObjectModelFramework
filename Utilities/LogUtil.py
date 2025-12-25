import logging
import os
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        log_dir = os.path.join(os.path.dirname(__file__), '../Logs')
        #os.makedirs(log_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas
        self.LogFileName = os.path.join(log_dir, f'log{curr_time}.txt')

        #self.LogFileName = '../Logs/log' + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
