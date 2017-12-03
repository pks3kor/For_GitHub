import logging
# Order: DEBUG, INFO, WARNING, ERROR and CRITICAL
logging.basicConfig(filename="sample.log", level=logging.DEBUG,filemode="w")
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")

#~ print logging.__builtins__
#~ a = 2
#~ b = 3
#~ print a
#~ print b
