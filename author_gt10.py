# -*- coding: utf-8 -*-
"""
5.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-27
lastModified: 
select authors from author_start_end_year.csv by the condition:
int(row[1]) >= 1993 and (int[row[2]] - int(row[1]) >= 10),
that is the author's first paper published year >= 1993 and academic career >= 10.
"""
import csv


author_gt10_list = list()
with open(r"author_start_end_year.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if int(row[1]) >= 1993 and (int(row[2]) - int(row[1]) >= 10):
            author_gt10_list.append(row)
print "author_gt10_list generate over"
print len(author_gt10_list)

with open(r"author_gt10.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_gt10_list)
print "result author_gt10.csv writes over"
