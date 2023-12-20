import logging

class logclass:
    
    def __init__(self, driver):
        self.driver = driver
        
    def getthelogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("Logs/logfile.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
