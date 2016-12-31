# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-25
lastModified: 2016-12-28

"""
import networkx as nx
import sys
import csv
import process
sys.path.append("..")
from conf import config


base_path = config.get_base_path()


def get_author_by_year(year, author_file_path):
    """
    get author_list by year.
    @type year: int value
    @param year: the 5th year from author's academic starts
    @type author_file_path: string value
    @param author_file_path: the authors we filtered(author_gt10_new.csv)
    return type: list object
    return value: the param's year is the 5th year's authors' list
    """
    author_list = list()
    with open(author_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if int(row[1]) <= year:
                author_list.append(row[0])
    print "author_list generates over in function: get_author_by_year"
    return author_list


def get_paper_citation_relation(year, paper_citation_relation_file_path):
    """
    get paper citing-cited relation of the param year.
    @type year: int value
    @param year: the 5th year from author's academic starts
    @type paper_citation_relation_file_path: string value
    @param paper_citation_relation_file_path: paper's citing-cited relation file(aps_full_info_citation.csv)
    return type: list object
    return value: paper doi's (citing-cited) tuple's list, [(citing, cited), (citing, cited), ...]
    """
    paper_citation_relation_list = list()
    with open(paper_citation_relation_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if reader.line_num % 10000 == 0:
                print reader.line_num
            if int(process.get_paper_year_by_doi(row[0])) <= year:
                if int(process.get_paper_year_by_doi(row[1])) <= year:
                    paper_citation_relation_list.append(row)
    print "paper_citation_relation_list generates over"
    return paper_citation_relation_list


def get_author_citation_network(year, paper_citation_relation_file_path):
    """
    get author citation network
    @type year: int value
    @param year: the 5th year from author's academic starts
    # @type author_file_path: string value
    # @param author_file_path: the authors we filtered(author_gt10_new.csv)
    @type paper_citation_relation_file_path: string value
    @param paper_citation_relation_file_path: paper's citing-cited relation file(aps_full_info_citation.csv)
    return type: networkx object
    return value: a directed graph of author citation network
    """
    paper_citation_relation_list = get_paper_citation_relation(year, paper_citation_relation_file_path)
    graph = nx.DiGraph()
    print "in creating graph"
    for citation_relation in paper_citation_relation_list:
        citing_author_list = process.get_author_list_by_doi(base_path, citation_relation[0])
        if len(citing_author_list) > 10:
            citing_author_list = citing_author_list[0: 10]
        cited_author_list = process.get_author_list_by_doi(base_path, citation_relation[1])
        if len(cited_author_list) > 10:
            cited_author_list = cited_author_list[0: 10]
        for citing_author in citing_author_list:
            if citing_author in cited_author_list:
                cited_author_list.remove(citing_author)
            for cited_author in cited_author_list:
                if graph.has_edge(citing_author, cited_author):
                    attr_dic = graph.get_edge_data(citing_author, cited_author)
                    attr_dic["weight"] += 1
                    graph.add_edge(citing_author, cited_author, attr_dict=attr_dic)
                else:
                    graph.add_edge(citing_author, cited_author, attr_dict={"weight": 1})
    return graph


if __name__ == '__main__':
    print "base_path: {}".format(base_path)
