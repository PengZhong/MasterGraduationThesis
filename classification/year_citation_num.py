# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-01-13
lastModified: 2017-04-17
according to the origin citation file aps-dataset-citations-2013.csv,
calculate citation numbers by year, and save result into csvfile(year, citation_num 2 columns)
"""
import os
import csv
import json
import sys
sys.path.append("..")
from conf import config
from aps import process


if os.name == "nt":
    base_path = config.base_path_nt
elif os.name == "posix":
    base_path = config.base_path_posix
else:
    print "error in get base_path, unknow os"
    exit(0)

year_citation_num_dic = dict()
origin_citation_path = os.path.join(base_path, r"../aps-dataset-citations-2013/aps-dataset-citations-2013.csv")
with open(origin_citation_path, "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    reader.next()
    for row in reader:
        year = process.get_paper_year_by_doi(row[1])
        if year in year_citation_num_dic:
            year_citation_num_dic[year] += 1
        else:
            year_citation_num_dic[year] = 1
        print reader.line_num
print year_citation_num_dic

with open(r"year_citation_num.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(year_citation_num_dic.iteritems())
print "year_citation_num.csv writes over"
