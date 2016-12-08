# -*- coding: utf-8 -*-
"""
character_3: author's average citation count in the first 5year
author: Zhong Peng
createDate: 2012-12-07
lastModified: 
according to author_citation_count.csv and author_paper_5year.csv, calculating
the average number of citations of the author's first 5 years publications.
"""
from __future__ import division
import csv
from collections import OrderedDict

author_list = list()
author_citation_count_dict = dict()
with open(r"author_citation_count.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_list.append(row[0])
        author_citation_count_dict[row[0]] = int(row[1])
print "author_citation_count_dict generates over"

author_paper_num_dict = dict()
with open(r"author_paper_num.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_paper_num_dict[row[0]] = int(row[1])
print "author_paper_num_dict generates over"

author_avg_citation_dict = OrderedDict()
for author in author_list:
    author_avg_citation_dict[author] = author_citation_count_dict[author] / author_paper_num_dict[author]
print "author_avg_citation_dict generates over"

with open(r"author_avg_citation_count.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_avg_citation_dict.iteritems())
print "result author_avg_citation_count.csv writes over"
