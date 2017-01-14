# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-01-13
lastModified: 
accoring to the aps_full_info_citation.csv, calculate every year's total citation number
and save it to total_citation_by_year.csv
"""
import csv
import sys
sys.path.append("..")
from aps import process


year_citation_count = dict()
with open(r"../aps_full_info_citation.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        print reader.line_num
        year = process.get_paper_year_by_doi(row[0])
        if year in year_citation_count:
            year_citation_count[year] += 1
        else:
            year_citation_count[year] = 1
print "year_citation_count generates over"

final_li = sorted(year_citation_count.iteritems(), key=lambda x:x[0])
with open(r"total_citation_by_year.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result total_citation_by_year.csv writes over"
