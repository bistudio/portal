import os
import re
import shutil as shu
import datetime as dt
import logging as log
from functools import lru_cache
from tkinter import *

# provide path to source folder

source_folder = "./source"

# get list of files in source folder

file_list = os.listdir(source_folder)
list_of_files = []

# remove unwanted process files

for list in file_list:
    file_ext_pat = re.compile(r'([a-zA-Z0-9_-]+?)\.([a-zA-Z0-9]+)')
    matches = file_ext_pat.finditer(list)
    for match in matches:
        if match.string == list:
            list_of_files.append(match.string)

# get the year and month of date file was modified

for file in list_of_files:
    file_time_seconds = os.path.getctime(source_folder+"/"+file)
    file_time = dt.datetime.fromtimestamp(file_time_seconds)
    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%B")
    file_year_month = file_month + " " + file_year
    file_year_dir = source_folder + "/" + file_year
    file_month_year_dir = source_folder + "/" + file_year + "/" + file_year_month
    try:
        os.mkdir(file_year_dir)  # created year of file
        os.mkdir(file_month_year_dir)  # created month of file
    except FileExistsError:
        pass
    try:
        os.mkdir(file_month_year_dir)
    except FileExistsError:
        pass

    # move the files into the correct folders

    try:
        shu.move(source_folder+"/"+file, file_month_year_dir)
    except FileNotFoundError:
        pass

    print(f'{file}, {file_year}, {file_year_month}, {source_folder+"/"+file}, {file_month_year_dir}')
