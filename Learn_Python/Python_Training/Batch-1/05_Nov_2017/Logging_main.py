# Main 

import logging
import module1
 
#----------------------------------------------------------------------
def main():
    """
    The main entry point of the application
    """
    #create a logger instance named "exampleApp"
    logger = logging.getLogger("exampleApp")
    #Set its logging level
    logger.setLevel(logging.INFO)
 
    # create the logging file handler to capture the logs
    fh = logging.FileHandler("sample1.log")
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    #The file handler has to set the formatter object as its formatter
    fh.setFormatter(formatter)
 
    # add handler to logger object
    logger.addHandler(fh)
 
    logger.info("Program started")
    result = module1.add(7, 8)
    logger.info("Done!")
 
if __name__ == "__main__":
    main()
    
    
    
    
# write module1


import logging
 
module_logger = logging.getLogger("exampleApp.otherMod2")
 
#----------------------------------------------------------------------
def add(x, y):
    """"""
    logger = logging.getLogger("exampleApp.otherMod2.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y