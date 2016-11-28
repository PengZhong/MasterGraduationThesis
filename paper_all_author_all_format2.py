# -*- coding: utf-8 -*-
"""
1.3
author: Zhong Peng(pengmany@outlook.com)
createDate: 2016-11-25
change the format of paper_all_author_all_format3.csv into format 2),
2) N columns: paper, authorA, authorB...., every author has stand in one column.
"""
import os
import csv
import json
from conf import config


if os.name == "posix":
    base_path = config.base_path_posix
elif os.name == "nt":
    base_path = config.base_path_nt
else:
    print "error in get base_path, unknow os"
    exit(0)

print base_path
# 2)
final_li = list()
for root, dirs, files in os.walk(base_path):
    for file in files:
        print file
        path = os.path.join(root, file)
        f = open(path, "rb")
        data = json.load(f)
        f.close()
        doi = data["id"].encode('utf-8')
        if not("authors" in data):
            final_li.append((doi, ""))
        else:
            authors = data["authors"]
            if len(authors) == 0:
                final_li.append((doi, ""))
            else:
                tmp_li = []
                tmp_li.append(doi)
                for au in authors:
                    if "name" in au:
                        author = au["name"].encode('utf-8').replace("\n", " ")
                        tmp_li.append(author)
                final_li.append(tmp_li)
print "final_li generate over"

with open(r"paper_all_author_all_format2.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result paper_all_author_all_format2.csv writes over"
