import os
import re
import shutil as shu
import datetime as dt
import logging as log
from tkinter import *
from flask import Flask

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


def get_files(fl):
    for list in fl:
        file_ext_pat = re.compile(r'([a-zA-Z0-9_-]+?)\.([a-zA-Z0-9]+)')
        matches = file_ext_pat.finditer(list)
        for match in matches:
            if match.string == list:
                list_of_files.append(match.string)


get_files(file_list)

if len(list_of_files) == 0:
    logger.info("No files found")
else:
    logger.info("list of files acquired")


def portal_file_utility(lof):
    # get the year and month of date file was modified
    for file in lof:
        file_extension = os.path.splitext(file)
        file_time_seconds = os.path.getctime(source_folder+"/"+file)
        file_time = dt.datetime.fromtimestamp(file_time_seconds)
        file_year = file_time.strftime("%Y")
        file_month = file_time.strftime("%B")
        file_year_month = file_month + " " + file_year
        file_year_dir = source_folder + "/" + file_year
        file_month_year_dir = source_folder + "/" + file_year + "/" + file_year_month
        ext = file_extension[-1].replace(".", "").capitalize()
        file_ext_dir = file_month_year_dir+"/"+ext

        try:
            os.mkdir(file_year_dir)  # created year of file
            logger.info("file year directory created")
        except FileExistsError:
            logger.info("year directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_month_year_dir)  # created month of file
            logger.info("file month directory created")
        except FileExistsError:
            logger.info("file month directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_ext_dir)  # create file extension directory
            logger.info("file extension directory created")
        except FileExistsError:
            logger.info("file extension directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_ext_dir)
            logger.info("file extension directory created")
        except FileExistsError:
            logger.info("file extension directory already exists - step skipped")
            pass

        # move the files into the correct folders

        try:
            if os.path.exists(file_ext_dir+'/'+file):
                pass
            else:
                shu.move(source_folder+"/"+file, file_ext_dir)
            logger.info("file(s) moved into file extension directory")
        except FileNotFoundError:
            logger.info("no files found to move - step skipped")
            pass


portal_file_utility(list_of_files)

list_of_files.clear()

# search each year folder for files to be moved

for year in os.listdir(source_folder):
    year_search_path = source_folder + '/' + year    # construct search path
    content = os.listdir(year_search_path)
    get_files(content)
    for file in list_of_files:
        file_extension = os.path.splitext(file)
        file_time_seconds = ''
        if not os.path.exists(year_search_path + "/" + file):
            pass
        else:
            file_time_seconds = os.path.getctime(year_search_path + "/" + file)
        try:
            file_time = dt.datetime.fromtimestamp(file_time_seconds)
            file_year = file_time.strftime("%Y")
            file_month = file_time.strftime("%B")
            file_year_month = file_month + " " + file_year
            file_year_dir = source_folder + "/" + file_year
            file_month_year_dir = source_folder + "/" + file_year + "/" + file_year_month
            ext = file_extension[-1].replace(".", "").capitalize()
            file_ext_dir = file_month_year_dir+"/"+ext
        except TypeError:
            pass

        try:
            os.mkdir(file_year_dir)  # created year of file
            logger.info("file year directory created")
        except FileExistsError:
            logger.info("year directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_month_year_dir)  # created month of file
            logger.info("file month directory created")
        except FileExistsError:
            logger.info("file month directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_ext_dir)  # create file extension directory
            logger.info("file extension directory created")
        except FileExistsError:
            logger.info("file extension directory already exists - step skipped")
            pass
        try:
            os.mkdir(file_ext_dir)
            logger.info("file extension directory created")
        except FileExistsError:
            logger.info("file extension directory already exists - step skipped")
            pass

        # move the files into the correct folders

        try:
            if os.path.exists(file_ext_dir+'/'+file):
                pass
            else:
                shu.move(year_search_path+"/"+file, file_ext_dir)
            logger.info("file(s) moved into file extension directory")
        except FileNotFoundError:
            logger.info("no files found to move - step skipped")
            pass


if len(list_of_files) == 0:
    logger.info("No files found")
else:
    logger.info("list of files acquired")


logger.info("portal application run completed - success")

