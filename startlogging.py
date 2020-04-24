import logging

class StartLogging:
    
    logging.basicConfig(filename='filetranfser.log',level=logging.INFO)  
    logging.info(" Logging started ")  
