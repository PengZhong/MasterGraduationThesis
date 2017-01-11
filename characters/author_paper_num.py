# -*- coding: utf-8 -*-
"""
character_1: author's paper number
author: Zhong Peng
createDate: 2016-11-30
lastModified: 
collect authors'(in author_gt10.csv) total paper number, 
after 5 years of their academic career's start.
"""
import csv


author_start_year_dict = dict()
author_count = 0
author_li = list()
with open(r"../author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_start_year_dict[row[0]] = int(row[1])
        author_li.append(row[0])
        author_count += 1
print "author_start_year_dict generate over"

author_paper_count_dict = dict()
with open(r"../author_all_year_list.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] in author_start_year_dict:
            start_year = author_start_year_dict[row[0]]
            paper_count = 0
            str_year_li = row[1][2: -2].split('\', \'')
            int_year_li = map(lambda x: int(x), str_year_li)
            for year in int_year_li:
                if year - start_year < 5:
                    paper_count += 1
            author_paper_count_dict[row[0]] = paper_count
print "author_paper_count_dict generate over"

final_li = sorted(author_paper_count_dict.iteritems(), key=lambda x: author_li.index(x[0]))
with open(r"author_paper_num.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result author_paper_num.csv writes over"
