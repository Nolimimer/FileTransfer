from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
from configreader import ConfigReader
from startlogging import StartLogging

import os
import time
import logging
import re

class DownloadFileHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if not(filename.startswith(".")):
                for pattern in sortDict.keys():
                    if re.search(pattern, filename):
                        logging.info(" Regex matched: " + pattern + " with Filename: " +  filename)
                        src = folder_to_track + "/" + filename
                        to = sortDict.get(pattern) + "/" + filename
                        try:
                            os.rename(src, to)
                            logging.info(" Moved " + src + " to " + to) 
                        except FileNotFoundError as Identifier:
                            logging.warning(Identifier)
                            logging.warning(" Please look at your destination path and whether the path exists. ")
                                 

# Config      
StartLogging()      
config = ConfigReader()
sortDict = config.getParams()
folder_to_track = config.getTrackFolder()

# Handling
eventHandler = DownloadFileHandler()
observer = Observer()
observer.schedule(eventHandler, folder_to_track, recursive =True)
observer.start()

try:
    while True:
        time.sleep(10)
        logging.info(" Running, timestamp: [" + str(time.asctime()) + "]")
except KeyboardInterrupt:
    observer.stop()

observer.join





