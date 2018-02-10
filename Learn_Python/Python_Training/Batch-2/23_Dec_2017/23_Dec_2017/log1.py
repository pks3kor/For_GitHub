#~ Level:
    #~ DEBUG
    #~ INFO
    #~ WARNING
    #~ ERROR
    #~ CRITICAL
import logging
# add filemode="w" to overwrite,default is append.'a'
logging.basicConfig(filename="sample.log", level=logging.CRITICAL,
format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', 
datefmt='%H:%M:%S')

logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("warning has happened!")
logging.error("An error has happened!")
logging.critical("A critical error has happened!")
