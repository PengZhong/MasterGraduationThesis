# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-014-17
lastModified: 2017-04-18
according to author_all_paper_li_all generates files that contains authors by year,
for example author_paper_2002.csv are authors whose 10th academic year is 2002
"""
import csv


author_paper_dic = dict()
with open(r"../author_all_paper_li_all.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    reader.next()
    for row in reader:
        author_paper_dic[row[0]] = row[1][2: -2].split("', '")
print "author_paper_dic generates over"

for year in range(1997, 2008):
    final_li = list()
    with open(r"../result/AuthorCitationNetwork/%s.csv" % year, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            tmp_li = list()
            author = row[0]
            tmp_li.append(author)
            tmp_li.append(author_paper_dic[author])
            final_li.append(tmp_li)
    print "year %s process over" % year
    save_path = r"../result/AuthorCitationByYear/author_paper_%s.csv" % (year + 5)
    with open(save_path, "wb") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerows(final_li)
    print "year %s result writes over" % year
