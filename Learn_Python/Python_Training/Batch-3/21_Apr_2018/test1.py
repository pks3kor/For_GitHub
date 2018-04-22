import logging
#~ DEBUG #~ INFO #~ WARNING #~ ERROR #~ CRITICAL 
logging.basicConfig(filename="test.log",level=logging.DEBUG,format= '%(asctime)s %(message)s', datefmt="%m_%d_%Y %H:%M:%S %p")
for i in range(1):
    logging.debug("This is debug message!!!")
    logging.info("This is info message!!!")
    logging.warning("This is warning message!!!")
    logging.error("This is error message!!!")
    logging.critical("This is critical message!!!")
