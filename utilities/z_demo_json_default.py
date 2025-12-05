import json
import csv
import os

from config import Config

js = json.load(open(os.path.join(Config.DATA_DIR, "config.json"), "r"))

print(js["browser"])
