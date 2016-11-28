# -*- coding: utf-8 -*-
"""
3.
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-26
according to author_paper_li_all.csv,
generate a csv file with 2 columns format: author_name, list of paper published year.
abandon the first line in author_all_paper_li_all.csv,
for this line is the set of all papers that lack of author information.
"""
import csv
import os
from aps import process
from conf import config


if os.name == "posix":
    base_path = config.base_path_posix
elif os.name == "nt":
    base_path = config.base_path_nt
else:
    print "error in get base_path, unknow os"
    exit(0)

author_year_list = list()
with open(r"author_all_paper_li_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    reader.next()
    for row in reader:
        print reader.line_num
        tmp_li = []
        tmp_li.append(row[0])
        doi_li = row[1][2: -2].split('\', \'')
        year_li = []
        for doi in doi_li:
            file_path = process.get_file_path_by_doi(base_path, doi)
            year = process.get_paper_year(file_path)
            year_li.append(year)
        tmp_li.append(year_li)
        author_year_list.append(tmp_li)
print "author_year_list generate over"

with open(r"author_all_year_list.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(author_year_list)
print "result author_year_list.csv writes over"
