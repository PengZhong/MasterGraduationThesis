# -*- coding: utf-8 -*-
"""
character_2.2: author's citation number
author: Zhong Peng
createDate: 2012-11-30
lastModified: 2012-12-07
save author's total citation count of the first 5 years into csv file
"""
import csv
import os
import sys
sys.path.append("..")
from aps import process
from conf import config
from collections import OrderedDict


if os.name == "posix":
    base_path = config.base_path_posix
elif os.name == "nt":
    base_path = config.base_path_nt
else:
    print "base_path init error"
    exit(0)

author_start_year_dict = dict()
with open(r"../author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_start_year_dict[row[0]] = int(row[1])
print "author_start_year_dict generates over"
# gen = author_start_year_dict.iteritems()
# print gen.next()
# print gen.next()
# print author_start_year_dict["U. van Kolck"]
# print "**********1111111111111*************"

doi_year_dict = dict()
with open(r"../doi_year.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        doi_year_dict[row[0]] = int(row[1])
print "doi_year_dict generates over"
# gen1 = doi_year_dict.iteritems()
# print gen1.next()
# print gen1.next()
# print doi_year_dict["10.1103/PhysRevC.49.2932"]
# print doi_year_dict["10.1103/PhysRevC.54.1523"]
# print "***********2222222222222**************"

paper_citation_dict = dict()
with open(r"../aps_full_info_citation.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        if row[1] in paper_citation_dict:
            paper_citation_dict[row[1]].append(row[0])
        else:
            paper_citation_dict[row[1]] = [row[0], ]
print "paper_citation_dict generates over"
# gen2 = paper_citation_dict.iteritems()
# print gen2.next()
# print gen2.next()
# print paper_citation_dict["10.1103/PhysRevC.49.2932"]
# for paper in paper_citation_dict["10.1103/PhysRevC.49.2932"]:
#     print paper, process.get_paper_year_by_doi(paper)
# print len(paper_citation_dict["10.1103/PhysRevC.49.2932"])
# print "**************33333333333333333*****************"

author_citation_5years_dict = OrderedDict()
err_count = 0
with open(r"author_paper_5year.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author = row[0]
        # if author != "U. van Kolck":
            # continue
        # print row
        cited_count = 0
        doi_li = row[1][2: -2].split('\', \'')
        # print "doi_li", doi_li
        start_year = author_start_year_dict[author]
        # print "start_year", start_year
        for doi in doi_li:
            if not(doi in paper_citation_dict):
                err_count += 1
                continue
            citing_doi_li = paper_citation_dict[doi]
            # print "citing_doi_li", doi, citing_doi_li, len(citing_doi_li)
            # print "-------------"
            for citing_doi in citing_doi_li:
                if abs(doi_year_dict[citing_doi] - start_year) < 5:
                    cited_count += 1
        author_citation_5years_dict[author] = cited_count
print "author_citation_5years_dict generates over"
# print author_citation_5years_dict
# print err_count
# exit(0)

with open(r"author_citation_count.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_citation_5years_dict.iteritems())
print "result author_citation_5years_dict writes over"
