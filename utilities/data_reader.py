# Module contains reusable methods to read data from excel, csv, json
import pandas


def get_sheet_into_list(excel_location, sheet_name):
    df = pandas.read_excel(io=excel_location, sheet_name=sheet_name)
    return df.values.tolist()
