import os
import shutil
from settings.settingBot import debug
from services.serviceLogger import consoleLogger as Logger

def clean(path):
    Logger.info("[CLEANER] Cleaning started")
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            if dirname == '__pycache__' or dirname == 'logs':
                if debug:
                    Logger.debug("[CLEANER] Deleting " + os.path.join(dirpath, dirname))
                shutil.rmtree(os.path.join(dirpath, dirname))
    Logger.info("[CLEANER] Cleaning done")
