# -*- coding: utf-8 -*-
"""
character_5: author's coauthor average citation number
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-12-08
lastModified: 2016-12-16
calculate author's coauthors' average citation number of first 5 years.
"""
import csv
import os
import sys
sys.path.append("..")
from collections import OrderedDict
from aps import CoauthorAvgCitation
from conf import config


base_path = config.get_base_path()

author_paper_file_path = r"../author_all_paper_li_all.csv"
paper_citation_file_path = r"../aps_full_info_citation.csv"
author_coauthor_avg_citation_dict = OrderedDict()
with open(r"../author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author = row[0]
        print author
        avg_citation = CoauthorAvgCitation.get_coauthor_avg_citation(author, author_paper_file_path, paper_citation_file_path, int(row[1]) + 4)
        author_coauthor_avg_citation_dict[author] = avg_citation
print "author_coauthor_avg_citation_dict generates over"

with open(r"coauthor_avg_citation_num.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_coauthor_avg_citation_dict.iteritems())
print "result coauthor_avg_citation_num.csv writes over"
