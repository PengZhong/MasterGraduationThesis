# -*- coding: utf-8 -*-
"""
character_2.2: (author's citation number)
author: Zhong Peng
createDate: 201-11-30
lastModified: 
save author's total citation count of the first 5 years into csv file
this file generates all dois list and all related citation relations(citing or cited) into csv file
"""
import csv
import sys
sys.path.append("..")
from aps import process
from conf import config

# get related paper list and init paper_5year_citation_count_dict
with open(r"paper_related.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        paper_li.append(row[0])
print "paper_li generates over"
paper_5year_citation_count_dict = {}.fromkeys(paper_li, 0)
print "paper_5year_citation_count_dict init over"

with open(r"new_citation.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[1] in paper_5year_citation_count_dict:
            if process.get_paper_year(row[1]) - process.get_paper_year(row[0]) < 5:
                paper_5year_citation_count_dict[row[1]] += 1
print "paper_5year_citation_count_dict generates over"

# save paper_5year_citationi_count into csv file
paper_5year_citation_li = sorted(paper_5year_citation_count_dict.iteritems(), key=lambda x: paper_li.index(x))
with open(r"paper_5year_citation_count.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(paper_5year_citation_li)
print "result paper_5year_citation_count writes over"
