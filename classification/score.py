# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-04-25
lastModified: 

"""
from __future__ import division
import csv


classification_method = "KNN"

precision_1 = 0.98
precision_2 = 0.998
precision_3 = 0.998
precision_4 = 0.915
precision_5 = 0.798
precision_6 = 0.691
precision_7 = 0.951

precision_sum = precision_1 + precision_2 + precision_3 + precision_4 + precision_5 + \
    precision_6 + precision_7
print "precision_sum:", precision_sum

weight_1 = precision_1 / precision_sum
weight_2 = precision_2 / precision_sum
weight_3 = precision_3 / precision_sum
weight_4 = precision_4 / precision_sum
weight_5 = precision_5 / precision_sum
weight_6 = precision_6 / precision_sum
weight_7 = precision_7 / precision_sum

print weight_1
print weight_2
print weight_3
print weight_4
print weight_5
print weight_6
print weight_7

score_li = list()
with open(r"author_characters.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        tmp_li = list()
        tmp_li.extend(row)
        score = weight_1 * int(row[1]) + weight_2 * int(row[2]) + weight_3 * float(row[3]) + weight_4 * int(row[4]) \
            + weight_5 * float(row[5]) + weight_6 * float(row[6]) + weight_7 * float(row[7])
        tmp_li.append(score)
        score_li.append(tmp_li)
print "score_li init over"

score_li.sort(key=lambda x: x[-1], reverse=True)
with open(r"sorted_author.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(score_li)
print "sorted_author.csv writes over"
