import logging

def logger(name):
    logging.basicConfig()
    log = logging.getLogger(name)
    log.setLevel(logging.INFO)
    
    return log