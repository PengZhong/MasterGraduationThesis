# -*- coding: utf-8 -*-
"""
character_2.1: (author's citation number)
author: Zhong Peng
createDate: 201-11-30
lastModified: 2011-12-01
save author's total citation count of the first 5 years into csv file
this file generates all dois list and all related citation relations(citing or cited) into csv file
"""
import csv
import os
import sys
sys.path.append("..")
from conf import config
from aps import process

if os.name == "posix":
    base_path = r"/media/zhongpeng/Datas/APS-DATA/aps-dataset-citations-2013/aps-dataset-citations-2013.csv"
elif os.name == "nt":
    base_path = r"E:\APS-DATA\aps-dataset-citations-2013\aps-dataset-citations-2013.csv"
else:
    print "base_path init error"
    exit(0)

# get all related paper(those writen by author_gt10)
paper_set = set()
with open(r"../author_all_paper_li_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        paper_li = row[1][2: -2].split('\', \'')
        paper_set.update(paper_li)
print "paper_set generates over"
print len(paper_set)

paper_related_list = map(lambda x: [x, ], list(paper_set))
with open(r"paper_related.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(paper_related_list)
print "paper_related.csv writes over"


# get related citation relation(those citing or cited paper in paper_related_list)
new_citation_list = list()
with open(base_path, "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[0] in paper_set or row[1] in paper_set:
            new_citation_list.append(row)
print "new_citation_list generates over"
print len(new_citation_list)

with open(r"new_citation.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(new_citation_list)
print "new_citation.csv writes over"
