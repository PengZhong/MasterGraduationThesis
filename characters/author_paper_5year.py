# -*- coding: utf-8 -*-
"""
character_2.1: author's citation number
author: Zhong Peng
createDate: 2012-11-30
lastModified: 2012-12-05
this program's target is generating author and papers those published in first 5 years 2 columns csv file
"""
import csv
from collections import OrderedDict
import sys
sys.path.append("..")
from aps import process


author_start_year_dict = dict()
with open(r"../author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_start_year_dict[row[0]] = int(row[1])
print "author_start_year_dict generates over"

author_paper_5year_dict = OrderedDict()
with open(r"../author_all_paper_li_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    reader.next()
    for row in reader:
        if row[0] in author_start_year_dict:
            tmp_li = list()
            doi_li = row[1][2: -2].split('\', \'')
            for doi in doi_li:
                year = int(process.get_paper_year_by_doi(doi))
                if abs(author_start_year_dict[row[0]] - year) < 5:
                    tmp_li.append(doi)
            author_paper_5year_dict[row[0]] = tmp_li
print "author_paper_5year_dict generates over"

with open(r"author_paper_5year.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_paper_5year_dict.iteritems())
print "result author_paper_5year.csv writes over"
