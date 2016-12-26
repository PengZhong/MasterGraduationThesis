# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-25
lastModified: 
in the result of character_5, we find that some authors are in the rear position in
the author list(not top 10 author), so we abort these authors and save new authors
in author_gt10_new.csv.
"""
import csv


new_author_list = list()
for year in range(1997, 2008):
    with open(r"./characters/%s.csv" % year, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            new_author_list.append(row[0])
print "new_author_list generates over"


final_li = list()
old_author_list = list()
with open(r"author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[0] in new_author_list:
            final_li.append(row)
            new_author_list.remove(row[0])
print "old_author_list generates over"


with open(r"author_gt10_new.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result author_gt10_new.csv writes over"
