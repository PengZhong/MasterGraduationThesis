# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-04-27
lastModified: 

"""
import csv


rank_author_li = list()
with open(r"rank_author.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        rank_author_li.append(row[0])
print "rank_author_li init over"

normalized_sorted_author_li = list()
with open(r"normalized_sorted_author.csv" ,"rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        normalized_sorted_author_li.append(row[0])
print "normalized_sorted_author_li init over"

# top = 0.001
# count = len(rank_author_li) * top
# print count
# int_count = int(count)
# print int_count
int_count = 2630
s = set(rank_author_li[0: int_count])
s.update(normalized_sorted_author_li[0: int_count])
res = 2 * int_count - len(s)
print res
