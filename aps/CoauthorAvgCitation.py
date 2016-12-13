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


def get_paper_li_by_author_name(author, year=0):
    """
    @input params:
    author: author's name
    year: 
    description: get author's paper list until the year(including)
    @output: author's all paper's doi list from start_year to end_year(including this year)
    """
    with open(r"../characters/author_paper_5year.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if row[0] == author:
                paper_li = row[1][2: -2].split('\', \'')
                break
    return paper_li


def get_coauthor_list(author, year=0):
    """
    @input params:
    author: author's name
    descriprion: get author's all coauthor until the year(including)
    @output: author's all coauthors from the academic start year to the start+time year
    """
    paper_li = get_paper_li_by_author_name(author)
    # print paper_li
    coauthor_set = set()
    for paper in paper_li:
        coauthor_set.update(process.get_author_list_by_doi(base_path, paper))
    coauthor_set.remove(author)
    return list(coauthor_set)


def get_all_coauthor_paper_list(coauthor_list, author_paper_file_path, year):
    """
    @input params:
    # author: author's name
    coauthor list: coauthor_list = get_coauthor_list(author)
    author_paper_file_path: the absolute path of author-paper(author_all_paper_li_all.csv) csv file
    year: collect papers published before this year(including the parameter year)
    description: get all coauthor's paper list by the end of the parameter year.
    @output: author's all coatuthor's doi list
    """
    # coauthor_list = get_coauthor_list(author)
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

def get_all_coauthor_paper_list2(author, author_paper_file_path, year):
    """
    @input params:
    author: author's name
    author_paper_file_path: the absolute path of author-paper(author_all_paper_li_all.csv) csv file
    year: collect papers published before this year(including the parameter year)
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


def get_cited_count(coauthor_paper_list, paper_citation_file_path, year):
    """
    @input params:
    coauthor_paper_list: a list of paper's doi
    paper_citation_file_path: incuding paper citing-cited relation's csv file(aps_full_info_citation.csv)
    year: a year(including this year)
    sum all paper's cited times until the parameter year.
    @output: a int number of total cited times in the paper list
    """
    cited_count = 0
    with open(paper_citation_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if row[1] in coauthor_paper_list:
                # print row[0]
                if int(process.get_paper_year_by_doi(row[0])) <= year:
                    cited_count += 1
    return cited_count


def get_coauthor_avg_citation(author, author_paper_file_path, paper_citation_file_path, year):
    """
    @input params:
    author: author's name
    author_paper_file_path: the absolute path of author-paper(author_all_paper_li_all.csv) csv file
    paper_citation_file_path: incuding paper citing-cited relation's csv file(aps_full_info_citation.csv)
    year: the end time of calculation
    description: calculate author's coauthor's average citation number until the year(including)
    @output: all author's coauthors' average citation(all citations / coauthor count)
    """
    coauthor_list = get_coauthor_list(author)
    coauthor_paper_list = get_all_coauthor_paper_list(coauthor_list, author_paper_file_path, year)
    total_cited_count = get_cited_count(coauthor_paper_list, paper_citation_file_path, year)
    # print "coauthor_list", coauthor_list
    # print "coauthor_paper_list", coauthor_paper_list
    # print "total_cited_count", total_cited_count
    if len(coauthor_list) == 0:
        return total_cited_count
    return total_cited_count / len(coauthor_list)


if __name__ == '__main__':
    li = get_coauthor_list("Charanjit S. Aulakh")
    path = r"../author_all_paper_li_all.csv"
    li1 = get_all_coauthor_paper_list(li, path, 2011)
    li2 = get_all_coauthor_paper_list2("Charanjit S. Aulakh", path, 2011)
    print li1 == li2
    print "*****************"
    citation_file_path = r"../aps_full_info_citation.csv"
    print get_cited_count(["10.1103/PhysRevB.32.7970", ], citation_file_path, 1989)
    print "*****************"
    author_paper_file_path = r"../author_all_paper_li_all.csv"
    paper_citation_file_path = citation_file_path
    with open(r"../author_gt10.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        # reader.next()
        for row in reader:
            print row[0], row[1]
            print get_coauthor_avg_citation(row[0], author_paper_file_path, paper_citation_file_path, int(row[1]) + 4)
            break
