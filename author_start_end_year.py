# -*- coding: utf-8 -*-
"""
4.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-26
lastModified: 2016-11-27
according to author_all_year_list.csv,
create file with author's name, academic start year and end year 3 columns format csv file
"""
import csv

final_list = list()
with open(r"author_all_year_list.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        tmp_list = []
        str_year_li = row[1][2: -2].split('\', \'')
        year_li = map(int, str_year_li)
        year_li.sort()
        tmp_list.append(row[0])
        tmp_list.append(year_li[0])
        tmp_list.append(year_li[-1])
        final_list.append(tmp_list)
print "final_list generate over"

with open(r"author_start_end_year.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_list)
print "result final_list writes over"
