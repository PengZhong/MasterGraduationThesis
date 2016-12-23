# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-14
lastModified: 2016-12-20

"""
from __future__ import division
import csv
import networkx as nx
import sys
sys.path.append("..")
from conf import config
import process
from collections import defaultdict
from RankAlgorithm import pagerank


# get metadata's absolute base path
base_path = config.get_base_path()

def get_all_related_paper_by_year(year, author_paper_file_path):
# def get_all_related_paper_by_author(author, year, author_paper_file_path):
    """
    get all related paper's doi list by author
    # @type author: string value
    # @param author: author's name
    @type year: int value
    @param year: the 5th year from author's academic start
    @type author_paper_file_path: string value
    @param author_paper_file_path: author-paper(author_all_paper_li_all.csv) csvfile's absolute path
    return type: list object
    return value: paper's doi list
    """
    related_paper_list = list()
    with open(author_paper_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            print reader.line_num
            paper_li = row[1][2: -2].split('\', \'')
            for paper in paper_li:
                if int(process.get_paper_year_by_doi(paper)) <= year:
                    related_paper_list.append(paper)
    return related_paper_list


def get_paper_rank_dict_by_year(year, related_paper_list, citation_file_path):
    """
    get paper's rank score in the citation netowrk of the year
    @type year: int value
    @param year: we use the data of the year to create coauthor network
    @type related_paper_list: string value
    @param related_paper_list: all related paper's doi list of the year
    @type citation_file_path: string value
    @param citation_file_path: paper citation relation file(aps_full_info_citation.csv)
    return type: dictionary object
    return value: a dictionary of paper's doi and rank score's key-value pairs of the year
    """
    rank_score_dict = dict()
    graph = nx.DiGraph()
    graph.add_nodes_from(related_paper_list)

    with open(citation_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            if int(process.get_paper_year_by_doi(row[0])) <= year:
                if int(process.get_paper_year_by_doi(row[1])) <= year:
                    graph.add_edge(row[0], row[1])
    rank_score_dict = pagerank.basic_pagerank_directed(graph)
    with open(r"../result/CoauthorNetwork/paper_rank_%s.csv" % year, "wb") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerows(rank_score_dict.iteritems())
    rank_score_dict = pagerank.basic_pagerank_directed(graph)
    return rank_score_dict


def create_coauthor_network(year, author_paper_file_path, citation_file_path):
# def create_coauthor_network(author, year, author_paper_file_path, paper_rank_dict):
    """
    create coauthor network of the author in the year.
    # @type author: string value
    # @param author: author name
    @type year: int value
    @param year: we use the data of the year to create coauthor network
    @type author_paper_file_path:string value
    @param author_paper_file_path: author-paper(author_all_paper_li_all.csv) csvfile's absolute path
    # @type paper_rank_dict: dictionary
    # @param paper_rank_dict: paper's score in citation netowrk
    @type citation_file_path: string value
    @param citation_file_path: paper citation relation file(aps_full_info_citation.csv)
    return type: a networkx object of directed network(two direction link between two nodes)
    return value: the coauthor network
    """
    sum_dict = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55}
    graph = nx.DiGraph()
    # related_paper_list = get_all_related_paper_by_author(author, year, author_paper_file_path)
    related_paper_list = get_all_related_paper_by_year(year, author_paper_file_path)
    paper_rank_dict = get_paper_rank_dict_by_year(year, related_paper_list, citation_file_path)
    for related_paper in related_paper_list:
        print related_paper
        author_list = process.get_author_list_by_doi(base_path, related_paper)
        length = len(author_list)
        if length == 0:
            continue
        if length > 10:
            length = 10
            author_list = author_list[0: 10]
        paper_value = paper_rank_dict[related_paper]
        for i in range(0, length):
            for j in range(i + 1, length):
                authorA = author_list[i]
                authorB = author_list[j]
                # add edge from A to B
                weight_dict_AB = graph.get_edge_data(authorA, authorB)
                if weight_dict_AB == {} or weight_dict_AB == None:
                    graph.add_edge(authorA, authorB, attr_dict={"weight": paper_value * (length - i) / sum_dict[length]})
                else:
                    weight_dict_AB["weight"] += paper_value * (length - i) / sum_dict[length]
                    graph.add_edge(authorA, authorB, attr_dict=weight_dict_AB)
                # add edge from B to A
                weight_dict_BA = graph.get_edge_data(authorB, authorA)
                if weight_dict_BA == {} or weight_dict_BA == None:
                    graph.add_edge(authorB, authorA, attr_dict={"weight": paper_value * (length - j) / sum_dict[length]})
                else:
                    weight_dict_BA["weight"] += paper_value * (length - j) / sum_dict[length]
                    graph.add_edge(authorB, authorA, attr_dict=weight_dict_BA)
    return graph


if __name__ == '__main__':
    print base_path
    paper_rank_dict = defaultdict(lambda : 1)
    author_paper_file_path = r"../author_all_paper_li_all.csv"
    citation_file_path = r"../aps_full_info_citation.csv"
    graph = create_coauthor_network(1997, author_paper_file_path, citation_file_path)
    print graph.number_of_nodes()
    print graph.number_of_edges()
