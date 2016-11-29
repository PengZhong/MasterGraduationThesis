# -*- coding: utf-8 -*-
"""
some useful functions of processing APS-DATA.
"""
import json
import os
import sys
sys.path.append("..")
from conf import config


def get_file_path_by_doi(base_path, doi):
    """
    input: base_path is the root path of the aps-metadata folder, doi is the paper's doi
    output: return the absolute path of the paper
    """
    path_dic = {"PhysRev":"PR", "PhysRevA":"PRA", "PhysRevB":"PRB", "PhysRevC":"PRC", \
        "PhysRevD":"PRD", "PhysRevE":"PRE", "PhysRevSeriesI":"PRI", "PhysRevLett":"PRL", \
        "PhysRevSTAB":"PRSTAB", "PhysRevSTPER":"PRSTPER", "PhysRevX":"PRX", "RevModPhys":"RMP"}
    li = doi.split(".")
    file_name = doi.split("/")[1] + ".json"
    file_path = os.path.join(base_path, path_dic[li[1][5: ]], li[2], file_name)
    return file_path


def get_paper_year(file_path):
    """
    input: the absolute json file path
    output: the paper's publish year if exist, or return None
    """
    f = open(file_path)
    data = json.load(f)
    f.close()
    if "date" in data:
        return data["date"][0: 4].encode('utf-8')
    else:
        return None


# about authors
def get_author_list_by_doi(base_path, doi):
    """
    input: base_path: metadata's absolute path, doi: the paper's doi
    output: the list of the paper's all author
    """
    file_path = get_file_path_by_doi(base_path, doi)
    f = open(file_path, "rb")
    data = json.load(f)
    f.close()
    author_li = list()
    try:
        authors = data["authors"]
        for au in authors:
            author_li.append(au["name"].encode("utf-8"))
    except:
        print "KeyError, please check the doi", doi
    return author_li


if __name__ == '__main__':
    doi = "10.1103/PhysRevA.23.52"
    base_path = config.base_path_posix
    file_path = get_file_path_by_doi(base_path, doi)
    print get_paper_year(file_path)
    print "***********************"
    print get_author_list_by_doi(base_path, "10.1103/PhysRevC.3.79")
