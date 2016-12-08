# -*- coding: utf-8 -*-
"""
character_4: author's coauthor count in first 5 year
author: Zhong Peng
createDate: 2012-12-07
lastModified: 
"""
import csv
import os
import sys
sys.path.append("..")
from aps import process
from conf import config
from collections import OrderedDict


if os.name == "nt":
    base_path = config.base_path_nt
elif os.name == "posix":
    base_path = config.base_path_posix
else:
    print "base_path init error, exit"
    exit(0)

author_coauthor_count_dict = OrderedDict()
with open(r"author_paper_5year.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        print row[0]
        coauthor_num = 0
        paper_li = row[1][2: -2].split('\', \'')
        for paper in paper_li:
            coauthor_num += len(process.get_author_list_by_doi(base_path, paper)) - 1
        author_coauthor_count_dict[row[0]] = coauthor_num
print "author_coauthor_count_dict generates over"

with open(r"author_coauthor_count.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_coauthor_count_dict.iteritems())
print "result author_coauthor_count.csv writes over"
