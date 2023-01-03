import datetime
import http.cookies

import dateutil.utils
import pandas as pd # could use more practice, but not bad
import csv # know decently well, just pick up what you don't know on documentation
import requests # probably won't be necessary in my job
from io import StringIO # practice is below
import pyodbc # practice is below
import urllib # Just look up the documentation. Not much going on with one
from sqlalchemy import create_engine # https://docs.sqlalchemy.org/en/20/core/engines.html
import glob # finds all the pathnames matching a specified pattern
import os # Just look up the documentation based on the code used. Lots going on here
import datetime as dt # also timedelta from datetime # Below shows some of what you can do. Check doc for more
import dateutil.relativedelta # Below shows some of what you can do. Check doc for more
import json # Not much for this one. Below is some of what you can do
import calendar # Check the doc. This has very good information
import http.client as httplib # 4 class types but client is most likely what you would use
import mimetypes # Not sure what it would do honestly
import sys
############################################################################################################
# Practice for io import StringIO
# string = 'This is a string'
#
# file = StringIO(string)
#
# print(file.read())
#
# file.write(" Welcome to geeksforgeeks.")
#
# file.seek(0)
#
# print('The string after writing is:', file.read())
################################################################################################################
# Practice for pyodbc
# cnxn_str = (
#             r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#             r'DBQ=C:\path\to\mydb.accdb;'
#             )
# cnxn = pyodbc.connect(cnxn_str, autocommit=True)
# crsr = cnxn.cursor() --check documentation for more explicit information
# crsr.execute(SQL STUFF)
##############################################################################################################
# Practice for glob
# glob_glob = glob.glob('Glob Directory/*.txt')
#
# for glob in sorted(glob_glob):
#    print(glob)
#######################################################################################################3#######
# This is practice for datetime and timedelta as well
#delta = datetime.timedelta(
#    days=50,
#    seconds=27,
#    microseconds=10,
#    milliseconds=29000,
#    minutes=5,
#    hours=8,
#    weeks=2
#)
#print(delta)
#print(delta.total_seconds())
#print(datetime.date)
#print(dateutil.utils.today())
##############################################################################################################
#json_stuff = '{"name":"John", "age":"30", "city":"New York"}'
#
#json_dump = json.loads(json_stuff)
#
#print(json_dump)
#
#json_stuff_2 = {"name": "John", "age": "30", "city": "New York"}
#
#dumpy = json.dumps(json_stuff_2)
#
#print(dumpy)
#############################################################################################################
#print(sys.modules)