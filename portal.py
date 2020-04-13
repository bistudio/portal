import os
import re
import shutil as shu
import datetime as dt
import logging as log
from tkinter import *


# configure logging level and output file

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
log.basicConfig(filename="./portal.log", level=log.DEBUG, format=LOG_FORMAT, filemode="w")
logger = log.getLogger()

# start logging activity

logger.info("Initiate logging activity")

# provide path to source folder

source_folder = "./source"
logger.info("Source folder specified")

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

if len(list_of_files) == 0:
    logger.info("No files found")
else:
    logger.info("list of files acquired")

# get the year and month of date file was modified

for file in list_of_files:
    file_extension = os.path.splitext(file)
    file_time_seconds = os.path.getctime(source_folder+"/"+file)
    file_time = dt.datetime.fromtimestamp(file_time_seconds)
    file_year = file_time.strftime("%Y")
    file_month = file_time.strftime("%B")
    file_year_month = file_month + " " + file_year
    file_year_dir = source_folder + "/" + file_year
    file_month_year_dir = source_folder + "/" + file_year + "/" + file_year_month
    file_ext_dir = file_month_year_dir+"/"+str(file_extension[-1]).capitalize().replace(".", "")
    try:
        os.mkdir(file_year_dir)  # created year of file
        os.mkdir(file_month_year_dir)  # created month of file
        os.mkdir(file_ext_dir)  # create file extension directory
        logger.info("file year, file year month and file extension directories created")
    except FileExistsError:
        logger.info("directories already exists - step skipped")
        pass

    try:
        os.mkdir(file_ext_dir)
        logger.info("file extension directory created")
    except FileExistsError:
        logger.info("file extension directory already exists - step skipped")
        pass

    # move the files into the correct folders

    try:
        shu.move(source_folder+"/"+file, file_ext_dir)
        logger.info("file(s) moved into file extension directory")
    except FileNotFoundError:
        logger.info("no files found to move - step skipped")
        pass

logger.info("portal application run completed - success")
