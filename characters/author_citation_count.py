# -*- coding: utf-8 -*-
"""
character_2: author's citation number
author: Zhong Peng
createDate: 201-11-30
lastModified: 
save author's total citation count of the first 5 years into csv file
"""
import csv
import os
import sys
sys.path.append("..")
from aps import process
from conf import config


if os.name == "posix":
    base_path = config.base_path_posix
elif os.name == "nt":
    base_path = config.base_path_nt
else:
    print "base_path init error"
    exit(0)

author_start_year_dict = dict()
with open(r"author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_start_year_dict[row[0]] = int(row[1])
print "author_start_year_dict generate over"

author_citation_count_dict = dict()
with open(r"author_gt10_paper_li.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        paper_li = row[1][2: -2].split('\', \'')
        for paper in paper_li:
            pass
