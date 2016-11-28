# -*- coding: utf-8 -*-
"""
6.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-27
lastModified: 
generate author, paper_li 2 columns files of author from author_gt10.csv
"""
import csv


author_li = list()
with open(r"author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_li.append(row[0])
print "author_li generate over"

final_li = list()
with open(r"author_all_paper_li_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[0] in author_li:
            final_li.append(row)
print "final_li generate over"

with open(r"author_gt10_paper_li.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result author_gt10_paper_li.csv writes over"
