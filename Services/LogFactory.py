import logging
class LogFactory:
    logger = None
    @staticmethod
    def Initialise(filePath):
        LogFactory.logger = logging.getLogger()
        LogFactory.logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler(filePath)
        fileHandler.setLevel(logging.INFO)
        consolHandler = logging.StreamHandler()
        consolHandler.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        fileHandler.setFormatter(formatter)
        consolHandler.setFormatter(formatter)
        LogFactory.logger.addHandler(consolHandler)
        LogFactory.logger.addHandler(fileHandler)