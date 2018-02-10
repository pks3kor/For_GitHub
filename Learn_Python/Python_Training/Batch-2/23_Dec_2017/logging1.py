import logging
# add filemode="w" to overwrite,default is append.'a'
logging.basicConfig(filename="sample.log", level=logging.DEBUG,
format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%H:%M:%S')
logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("An error has happened!")
logging.error("An error has happened!")
logging.critical("An error has happened!")
