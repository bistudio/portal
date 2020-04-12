import os
import re
import shutil as shu
import datetime as dt
import logging as log
from functools import lru_cache
from tkinter import *

# file_ico_copy = shu.copy("./file_1.ico", "./source")
# with open("./source/text_file.txt", "a") as f:
#     for i in range(6, 10):
#         f.write(f'This is line {i}\n')

# create log file


# provide path to source folder

source_folder = "./source"

# get list of files in source folder

file_list = os.listdir(source_folder)
# file_list.remove(list_of_files[0])
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
    st = os.stat(source_folder+"/"+file)
    file_time = dt.datetime.fromtimestamp(st.st_ctime)
    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%B")
    file_year_month = file_month + " " + file_year
    file_year_dir = source_folder + "/" + file_year
    file_month_year_dir = source_folder + "/" + file_year + "/" + file_year_month
    try:
        os.mkdir(file_year_dir)
        os.mkdir(file_month_year_dir)
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

# log activities

log.basicConfig(filename="./portal.log", level=log.CRITICAL)
log.basicConfig(filename="./portal.log", level=log.WARNING)
log.basicConfig(filename="./portal.log", level=log.INFO)
