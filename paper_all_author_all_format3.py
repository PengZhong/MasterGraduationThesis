# -*- coding: utf-8 -*-
"""
1.2
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-25
change the format of paper_all_author_all_format3.csv into format 3),
3) two columns: paper, author, and every row represents a pair of one paper and one author,
    e.t. each paper P has 3 authors(A, B, C), then there're 3 lines: (P, A), (P, B), (P, C)
"""
import csv


final_li = list()
with open(r"paper_all_author_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        tmp_li = []
        tmp_li.append(row[0])
        tmp_li.append(row[1].replace("\n", " "))
        final_li.append(tmp_li)
print "final_li generate over"

with open(r"paper_all_author_all_format3.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result paper_all_author_all_format3.csv writes over"
