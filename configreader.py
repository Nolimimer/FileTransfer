import configparser
import logging

# Read Config File
class ConfigReader: 

    __sortDict = {
    }
    __trackFolder = ""   

    _config = configparser.ConfigParser()
    _config.sections()
    try:  
        _config.read('params.config')
    except configparser.ParsingError as identifier:
        logging.fatal(identifier)

    for key in _config['KeyValue']:
        __sortDict[key] = _config['KeyValue'][key]

    for key in _config['Directory']:
         __trackFolder = _config['Directory'][key]

    def getTrackFolder(self):
        return self.__trackFolder

    def getParams(self):
        return self.__sortDict