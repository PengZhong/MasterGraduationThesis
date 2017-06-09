# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-04-19
lastModified: 2017-04-19
sort all authors by his citation numbers' percentage in his 10th year.
"""
from __future__ import division
import csv


year_citation_num_dic = dict()
with open(r"year_citation_num.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        year_citation_num_dic[row[0]] = int(row[1])
print "year_citation_num_dic generates over"
print year_citation_num_dic

# final_li = [[author_name, year, percentage of citation], ]
final_li = list()
for year in xrange(2002, 2013):
    print "year:", year
    total_citation = year_citation_num_dic[str(year)]
    with open(r"../result/AuthorCitationByYear/author_citation_%s.csv" % year, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            tmp_li = list()
            tmp_li.append(row[0])
            tmp_li.append(year)
            tmp_li.append(int(row[1]) / total_citation)
            final_li.append(tmp_li)
    print "year {} process over".format(year)

print "final_li init over"

final_li.sort(key=lambda x: x[2], reverse=True)

print "final_li sort over"

with open(r"rank_author.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "rank_author.csv save over"
