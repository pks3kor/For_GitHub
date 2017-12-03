import logging
#~ import pdb

# Order: DEBUG, INFO, WARNING, ERROR and CRITICAL
logging.basicConfig(filename="sample.log", level=logging.INFO)
#~ logging.basicConfig( filemode="w",filename='somelog.log', level=logging.WARNING, format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s', datefmt='%H:%M:%S' )
#~ pdb.set_trace()
logging.error("This is a debug message")
logging.debug("This is a debug message")
logging.info("Informational message")
logging.warning("An error has happened!")
logging.critical("Informational message")

a = 2
b = 3
print a
print b
