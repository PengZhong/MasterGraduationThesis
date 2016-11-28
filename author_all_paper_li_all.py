# -*- coding: utf-8 -*-
"""
2.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-26
generate author-paper_li 2 columns format csv file,
according to the paper_all_author_all.csv
"""
import csv


author_paper_dict = dict()
with open(r"paper_all_author_all_format3.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[1] in author_paper_dict:
            author_paper_dict[row[1]].append(row[0])
        else:
            author_paper_dict[row[1]] = [row[0], ]
print "author_paper_dict generate over"

with open(r"author_all_paper_li_all.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_paper_dict.iteritems())
print "result author_all_paper_li_all.csv writes over"
