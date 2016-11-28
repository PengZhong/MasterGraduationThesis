# -*- coding: utf-8 -*-
"""
1.4
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-25
change the format of paper_all_author_all_format3.csv into format 1),
1) two columns: paper, author list of string type, and every row represents one paper(doi)
"""
import csv


paper_author_li_dict = dict()
with open(r"paper_all_author_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[0] in paper_author_li_dict:
            paper_author_li_dict[row[0]].append(row[1].replace("\n", " ").decode('utf-8'))
        else:
            paper_author_li_dict[row[0]] = [row[1].replace("\n", " ").decode('utf-8'), ]
print "paper_author_li_dict generate over"

with open(r"paper_all_author_all_format1.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(paper_author_li_dict.iteritems())
print "result paper_all_author_all_format1.csv writes over"
