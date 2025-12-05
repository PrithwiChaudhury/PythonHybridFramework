import os.path
import config
from config import Config

from utilities import data_reader


class DataSource:
    data_invalid_login = [("John", "John123", "Invalid credentials"),
                          ("Saul", "Saul123", "Invalid credentials")]

    data_valid_login = [("Admin", "admin123")]

    data_invalid_login_excel = data_reader.get_sheet_into_list(os.path.join(Config.DATA_DIR, "test_data_sheet.xlsx"),
                                                                            "test_invalid_login")


