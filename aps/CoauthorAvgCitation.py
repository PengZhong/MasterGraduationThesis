# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-10
lastModified: 
version: 1.0
"""
from __future__ import division
import csv
import process
import sys
sys.path.append("..")
from conf import config


base_path = config.get_base_path()


def get_paper_li_by_author_name(author, start_year=0, end_year=0):
    """
    @input params:
    author: author's name
    start_year: the start year of calculation
    end_year: the end year of calculation(including this year)
    @output: author's all paper's doi list from start_year to end_year(including this year)
    """
    with open(r"../characters/author_paper_5year.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if row[0] == author:
                paper_li = row[1][2: -2].split('\', \'')
                break
    return paper_li


def get_coauthor_list(author):
    """
    @input params:
    author: author's name
    @output: author's all coauthors from the academic start year to the start+time year
    """
    paper_li = get_paper_li_by_author_name(author)
    print paper_li
    coauthor_set = set()
    for paper in paper_li:
        coauthor_set.update(process.get_author_list_by_doi(base_path, paper))
    coauthor_set.remove(author)
    return list(coauthor_set)


def get_all_coauthor's paper_list(author):
    """
    @input params:
    author: author's name
    @output: author's all coatuthor's doi list
    """
    pass


def get_coauthor_avg_citation(author, start_year, year=4):
    """
    @input params:
    author: author's name
    start_year: author's academic start year
    year: the time period of calculation(year=4, calculate the first 5 years' data e.g.)
    @output: all author's coauthors' average citation(all citations / coauthor count)
    """
    pass


if __name__ == '__main__':
    li = get_coauthor_list("Charanjit S. Aulakh")
    print li
    print len(li)
