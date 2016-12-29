# -*- coding: utf-8 -*-
"""
character_7: author's value in author citing-cited network(according paper citation relation)
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-25
lastModified: 2016-12-18

"""
import csv
import sys
sys.path.append("..")
from aps import AuthorCitationNetwork
from RankAlgorithm import pagerank


year_author_dict = dict()
with open(r"../author_gt10_new.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        year = int(row[1]) + 4
        if year_author_dict.has_key(year):
            year_author_dict[year].append(row[0])
        else:
            year_author_dict[year] = [row[0], ]
print "year_author_dict generates over"


paper_citation_relation_file_path = r"../aps_full_info_citation.csv"
# 1994 + 4 ~ 2003 + 4(including this year)
for year in range(1997, 2008):
    print year
    author_value_dict = dict()
    # call graph creation function
    graph = AuthorCitationNetwork.get_author_citation_network(year, paper_citation_relation_file_path)
    # rank graph node
    rank_value = pagerank.weighted_pagerank_directed_author_citation_network(graph)
    for author in year_author_dict[year]:
        print author
        author_value_dict[author] = rank_value[author]
    with open(r"../result/AuthorCitationNetwork/%s.csv" % year, "wb") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerows(author_value_dict.iteritems())
    print "result of the year {} writes over".format(year)


if __name__ == '__main__':
    print "test"
