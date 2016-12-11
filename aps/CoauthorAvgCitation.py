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
    # print paper_li
    coauthor_set = set()
    for paper in paper_li:
        coauthor_set.update(process.get_author_list_by_doi(base_path, paper))
    coauthor_set.remove(author)
    return list(coauthor_set)


def get_all_coauthor_paper_list(author, author_paper_file_path, year):
    """
    @input params:
    author: author's name
    author_paper_file_path: the absolute path of author-paper csv file
    year: year
    description: get all coauthor's paper list by the end of the parameter year.
    @output: author's all coatuthor's doi list
    """
    coauthor_list = get_coauthor_list(author)
    all_paper_list = list()
    with open(author_paper_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if row[0] in coauthor_list:
                paper_li = row[1][2: -2].split('\', \'')
                for paper in paper_li:
                    if int(process.get_paper_year_by_doi(paper)) <= year:
                        all_paper_list.append(paper)
                coauthor_list.remove(row[0])
                break
    return all_paper_list


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
    path = r"../author_all_paper_li_all.csv"
    print get_all_coauthor_paper_list("Charanjit S. Aulakh", path, 2011)
