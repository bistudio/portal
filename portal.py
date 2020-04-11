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

# provide path to source folder

source_folder = "./source"

# get list of files in source folder

list_of_files = os.listdir(source_folder)

# get the year and month of date file was modified

for file in list_of_files:
    st = os.stat(source_folder+"/"+file)
    file_time = dt.datetime.fromtimestamp(st.st_ctime)
    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%B")
    file_year_month = file_month + " " + file_year
    try:
        os.mkdir(source_folder + "/" + file_year)
        os.mkdir(source_folder + "/" + file_year + "/" + file_year_month)
    except FileExistsError:
        pass
    try:
        os.mkdir(source_folder + "/" + file_year + "/" + file_year_month)
    except FileExistsError:
        pass

    print(f'{file}, {file_year}, {file_year_month}')



