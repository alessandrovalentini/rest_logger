import logging

def setupLogger():
    logging.basicConfig(
        level=logging.WARN,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.StreamHandler()
        ])
    return logging.getLogger()

def simpleLogger():
    return logging.getLogger()