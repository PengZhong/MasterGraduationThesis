# -*- coding: utf-8 -*-
"""
author: Zhong Peng
createDate: 2017-04-20
lastModified: 2017-04-21
merge all characters in one csvfile
"""
import csv

# character_1
author_paper_num_dic = dict()
with open(r"../characters/author_paper_num.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_paper_num_dic[row[0]] = int(row[1])
print "author_paper_num_dic generates over"

# character_2
author_citation_count_dic = dict()
with open(r"../characters/author_citation_count.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_citation_count_dic[row[0]] = int(row[1])
print "author_citation_count_dic generates over"

# character_3
author_avg_citation_count_dic = dict()
with open(r"../characters/author_avg_citation_count.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_avg_citation_count_dic[row[0]] = float(row[1])
print "author_avg_citation_count_dic generates over"

# character_4
author_coauthor_count_dic = dict()
with open(r"../characters/author_coauthor_count.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        author_coauthor_count_dic[row[0]] = int(row[1])
print "author_coauthor_count_dic generates over"

# character_5
coauthor_avg_citation_num_dic = dict()
with open(r"../characters/coauthor_avg_citation_num.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        coauthor_avg_citation_num_dic[row[0]] = float(row[1])
print "coauthor_avg_citation_num_dic generates over"

# character_6
coauthor_network_score_dic = dict()
for year in xrange(1997, 2008):
    with open(r"../result/CoauthorNetwork/%s.csv" % year, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            coauthor_network_score_dic[row[0]] = float(row[1])
print "coauthor_network_sore_dic generates over"

# character_7
citation_network_score_dic = dict()
for year in xrange(1997, 2008):
    with open(r"../result/AuthorCitationNetwork/%s.csv" % year, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            citation_network_score_dic[row[0]] = float(row[1])
print "citation_network_score_dic generates over"

# final_li = [[author_name, char_1, char_2, char_3, char_4, char_5, char_6, char_7], ]
final_li = list()
with open(r"rank_author.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        tmp_li = list()
        author = row[0]
        tmp_li.append(author)
        tmp_li.append(author_paper_num_dic[author])
        tmp_li.append(author_citation_count_dic[author])
        tmp_li.append(author_avg_citation_count_dic[author])
        tmp_li.append(author_coauthor_count_dic[author])
        tmp_li.append(coauthor_avg_citation_num_dic[author])
        tmp_li.append(coauthor_network_score_dic[author])
        tmp_li.append(citation_network_score_dic[author])
        final_li.append(tmp_li)
print "final_li generates over"

with open(r"author_characters.csv", "wb") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")
    writer.writerows(final_li)
print "result author_characters.csv save over"
