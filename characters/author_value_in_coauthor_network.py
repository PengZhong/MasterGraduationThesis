# -*- coding: utf-8 -*-
"""
character_6: author's rank value in coauthor network
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-17
lastModified: 2016-12-20
calculate every author's score value in coauthor network of his(her) 5th academic year.
we calculate this value by the year and then extract authors whose 5th year ofacademic
career is the year. And then save the value in author_value_in_coauthor_network.csv
(note: in the whole experiment, we select the authors whose academic start year is 
    between 1993 and 2003(including), so we calculate this character value from year 
    1997(1993 + 4) to 2007(2003 + 4) directly without any calculattion.)
"""
import csv
import sys
sys.path.append("..")
from aps import CoauthorNetwork
from RankAlgorithm import pagerank


year_author_dict = dict()
with open(r"../author_gt10.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")
    for row in reader:
        year = int(row[1]) + 4
        if year in year_author_dict:
            year_author_dict[year].append(row[0])
        else:
            year_author_dict[year] = [row[0], ]
print "year_author_dict generates over"

author_paper_file_path = r"../author_all_paper_li_all.csv"
citation_file_path = r"../aps_full_info_citation.csv"
for year in range(1997, 2008):
    author_value_dict = dict()
    graph = CoauthorNetwork.create_coauthor_network(year, author_paper_file_path, citation_file_path)

    # call weighted pagerank algorithm, return rank_value_dict
    rank_value_dict = pagerank.weighted_pagerank_directed_coauthor_network(graph)

    for author in year_author_dict[year]:
        author_value_dict[author] = rank_value_dict[author]

    # save result
    with open(r"%s.csv" % year, "wb") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerows(author_value_dict.iteritems())
    print "result %s.csv writes over" % year
