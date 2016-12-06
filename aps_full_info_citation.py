# -*- coding: utf-8 -*-
"""
7.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-12-05
lastModified: 
filter citation records, abandon the records that the related(citing or cited) paper's 
info(author info and publish year) are not complete.
results are two files:
1) doi_year.csv which includes (doi, year) info of each row(only papers that has full info are laoded).
2) aps_full_info_citation.py which includes 'all'(the remains) papers' citation relation.
"""
import csv
import os
from aps import process
from collections import OrderedDict


if os.name == "posix":
    citation_path = r"/media/zhongpeng/Datas/APS-DATA/aps-dataset-citations-2013/aps-dataset-citations-2013.csv"
elif os.name == "nt":
    citation_path = r"E:\APS-DATA\aps-dataset-citations-2013\aps-dataset-citations-2013.csv"
else:
    print "citation_path init error"
    exit(0)

# save doi-year info into a two columns' csv file
doi_year_dict = OrderedDict()
new_citation_li = list()
with open(citation_path, "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    reader.next()
    for row in reader:
        print reader.line_num
        # process row[0]
        if not(row[0] in doi_year_dict):
            try:
                year = int(process.get_paper_year_by_doi(row[0]))
            except IOError as e:
                print "IOError in {}".format(reader.line_num)
                continue
            if 0 < year < 2013:
                doi_year_dict[row[0]] = year
        # process row[1]
        if not(row[1] in doi_year_dict):
            try:
                year = int(process.get_paper_year_by_doi(row[1]))
            except IOError as e:
                print "IOError in {}".format(reader.line_num)
                continue
            if 0 < year < 2013:
                doi_year_dict[row[1]] = year
        # process row
        if row[0] in doi_year_dict and row[1] in doi_year_dict:
            new_citation_li.append(row)
print "doi_year_dict generates over"

# write doi-year csv file
with open(r"doi_year.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(doi_year_dict.iteritems())
print "doi_year.csv writes over"

# write new_citation csv file
with open("aps_full_info_citation.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(new_citation_li)
print "result aps_full_info_citation.csv writes over"
