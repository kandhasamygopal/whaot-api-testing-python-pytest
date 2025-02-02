 # Helper functions for common test utilities
from utils.config import BASE_URL ,AUTH_HEADERS
import csv
import os


def read_credentials(file_path):
    abs_path = os.path.abspath(file_path)
    with open (abs_path,"r") as file:
       csv_reader= csv.DictReader(file)
       credentials = [row for row in csv_reader]
       return credentials