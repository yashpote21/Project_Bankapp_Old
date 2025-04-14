import inspect
import logging

class Log_Class:

    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]

        logger = logging.getLogger(name)
        file = logging.FileHandler(".\\Logs\\BankApp.log")
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        file.setFormatter(logformat)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger