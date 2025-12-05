# Module contains reusable methods to read data from excel, csv, json
import pandas
from config import Config
import json
import os


def get_sheet_into_list(excel_location, sheet_name):
    df = pandas.read_excel(io=excel_location, sheet_name=sheet_name)
    return df.values.tolist()


def get_csv_into_list(csv_location):
    df = pandas.read_csv(csv_location, delimitter=";")
    return df.values.tolist()


def get_value_from_json_config(key: str):
    js = json.load(open(os.path.join(Config.DATA_DIR, "config.json"), "r"))
    return js[key]


def get_value_from_json(json_path, key: str):
    js = json.load(open(json_path, "r"))
    return js[key]
