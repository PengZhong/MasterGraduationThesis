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
from aps import process


base_path = r"/media/zhongpeng/Datas/APS-DATA/aps-dataset-metadata-2013"
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
