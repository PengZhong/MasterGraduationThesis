# -*- coding: utf-8 -*-
"""
character_5: author's coauthor average citation number
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-12-08
lastModified: 
calculate author's coauthors' average citation number of first 5 years.
"""
import csv
import os
import sys
sys.path.append("..")
from collections import OrderedDict
from aps import process
from conf import config


base_path = config.get_base_path()

author_coauthor_dict = OrderedDict()
with open(r"author_paper_5year.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        print row[0]
        coauthor_set = set()
        paper_li = row[1][2: -2].split('\', \'')
        for paper in paper_li:
            coauthor_set.update(process.get_author_list_by_doi(base_path, paper))
        author_coauthor_dict[row[0]] = list(coauthor_set)
print "author_coauthor_dict generates over"

