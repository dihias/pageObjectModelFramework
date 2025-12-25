from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))

import os

def readConfig(section, key):
    config = ConfigParser()
    # make path relative to this file
    path = os.path.join(os.path.dirname(__file__), "../ConfigurationData/conf.ini")
    print("Reading config from:", os.path.abspath(path))
    read_files = config.read(path)
    print("Files read:", read_files)
    return config.get(section, key)