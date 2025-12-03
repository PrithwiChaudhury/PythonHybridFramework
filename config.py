import os


# print(os.path.abspath(__file__))

# print(os.path.dirname(os.path.abspath(__file__)))
class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(ROOT_DIR, "test_data")
    REPORT_DIR = os.path.join(ROOT_DIR, "report")


print(Config.DATA_DIR)
