# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-14
lastModified: 

"""
import csv
import networkx as nx
import sys
sys.path.append("..")
from conf import config
import process


# get metadata's absolute base path
base_path = config.get_base_path()


def get_all_related_paper_by_author(author, year, author_paper_file_path):
    """
    get all related paper's doi list by author
    @type author: string value
    @param author: author's name
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
            paper_li = row[1][2: -2].split('\', \'')
            for paper in paper_li:
                if int(process.get_paper_year_by_doi(paper)) <= year:
                    related_paper_list.append(paper)
    return related_paper_list


# def get_edge_weight(authorA, authorB, author_paper_dict, paper_rank_dict):
#     """
#     calculate authorA's and authorB's edge weight(attr_dict)
#     @type authorA: string value
#     @param authorA: authorA's name
#     @type authorB: string value
#     @param authorB: authorB's name
#     @type author_paper_dict: dictionary
#     @param author_paper_dict: author-paper's dictionary, key is author, value is paper list(string type)
#     @type paper_rank_dict: dictionary
#     @param paper_rank_dict: paper's score in citation netowrk
#     return type: numerical value
#     return value: the edge weight value between the node authorA and authorB
#     """
#     paper_listA = author_paper_dict[authorA]
#     paper_listB = author_paper_dict[authorB]
#     paper_setA = set(paper_listA)
#     paper_setB = set(paper_listB)
#     coauthor_paper_set = paper_setA & paper_setB
#     for paper in coauthor_paper_set:
#         author_list = process.get_author_list_by_doi(paper)
#         paper_value = paper_rank_dict[paper]
#         orA = author_list.index(authorA)
#         orB = author_list.index(authorB)
#         pass
#     return edge_weight


def create_coauthor_network(author, year, author_paper_file_path, paper_rank_dict):
    """
    create coauthor network of the author in the year.
    @type author: string value
    @param author: author name
    @type year: int value
    @param year: we use the data of the year to create coauthor network
    @type author_paper_file_path:string value
    @param author_paper_file_path: author-paper(author_all_paper_li_all.csv) csvfile's absolute path
    @type paper_rank_dict: dictionary
    @param paper_rank_dict: paper's score in citation netowrk
    return type: a networkx object of directed network(two direction link between two nodes)
    return value: the coauthor network
    """
    sum_dict = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55}
    graph = nx.DiGraph()
    related_paper_list = get_all_related_paper_by_author(author, year, author_paper_file_path)
    for related_paper in related_paper_list:
        author_list = process.get_author_list_by_doi(base_path, related_paper)
        length = len(author_list)
        if length > 10:
            length == 10
            author_list = author_list[0: 10]
        paper_value = paper_rank_dict[related_paper]
        for i in range(0, length):
            for j in range(i + 1, length + 1):
                authorA = author_list[i]
                authorB = author_list[j]
                # add edge from A to B
                weight_dict_AB = graph.get_edge_data(authorA, authorB)
                if weight_dict_AB == {}:
                    graph.add_edge(authorA, authorB, attr_dict={"weight": paper_value * (i + 1) / sum_dict[length]})
                else:
                    weight_dict_AB["weight"] += paper_value * (i + 1) / sum_dict[length]
                    graph.add_edge(authorA, authorB, attr_dict=weight_dict_AB)
                # add edge from B to A
                weight_dict_BA = graph.get_edge_data(authorB, authorA)
                if weight_dict_BA == {}:
                    graph.add_edge(authorB, authorA, attr_dict={"weight": paper_value * (j + 1) / sum_dict[length]})
                else:
                    weight_dict_BA["weight"] += paper_value * (j + 1) / sum_dict[length]
                    graph.add_edge(authorB, authorA, attr_dict=weight_dict_BA)
    return graph


if __name__ == '__main__':
    print base_path
