# -*- coding: utf-8 -*-
"""
author: Zhong Peng (pengmany@outlook.com)
createDate: 2016-12-13
lastModified: 2016-12-14

"""
from __future__ import division
import networkx as nx


def basic_pagerank_directed(graph, damping_factor=0.85, max_iterations=20, min_delta=0.0001):
    """
    basic pagerank algorithm in directed network and calculation by formular(not matrix).
    @type graph: netowrkx object of directed network
    @param graph: a digraph object
    @type graph: float value
    @param famping_factor: damping factor in pagerank algorithm, default value is 0.85
    @type max_iterations: int value
    @param max_iterations: max iteration times in the loop of pagerank in case of the 
        algorithm doesn't converge
    @type min_delta: float value
    @param min_delta: when the distance of the sum of all PR value of two iteration is 
        less than this value, we say the algorithm converges
    @return: the dictionary of all nodes' PR value
    """
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty netowrk, return {}"
        return {}
    
    rank_value_dict = {}.fromkeys(nodes, 1 / graph_size)
    min_value = (1 - damping_factor) / graph_size

    for time in xrange(1, max_iterations + 1):
        print "Iteration time(start): {}".format(time)
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for in_node in graph.predecessors(node):
                rank_score += damping_factor * rank_value_dict[in_node] / len(graph.successors(in_node))
            diff += abs(rank_score - rank_value_dict[node])
            rank[node] = rank_score
        print "Iteration time(end): {}".format(time)
        if diff < min_delta:
            print "algorithm converge!"
            break
    print "pagerank algorithm calculate over"
    return rank_value_dict


def basic_pagerank_undirected(graph, damping_factor=0.85, max_iterations=20, min_delta=0.0001):
    """
    basic pagerank algorithm in undirected network and calculation by formular(not matrix).
    @type graph: netowrkx object of undirected network
    @param graph: a undirected netowrkx object
    @type graph: float value
    @param famping_factor: damping factor in pagerank algorithm, default value is 0.85
    @type max_iterations: int value
    @param max_iterations: max iteration times in the loop of pagerank in case of the 
        algorithm doesn't converge
    @type min_delta: float value
    @param min_delta: when the distance of the sum of all PR value of two iteration is 
        less than this value, we say the algorithm converges
    @return: the dictionary of all nodes' PR value
    """
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        print "empty netowrk, return {}"
        return {}

    rank_value_dict = {}.fromkeys(nodes, 1 / graph_size)
    min_value = (1 - damping_factor) / graph_size

    for time in range(1, max_iterations + 1):
        print "Iteration time(start): {}".format(time)
        diff = 0.0
        for node in nodes:
            rank_score = min_value
            for neighbor in graph.neighbors(node):
                rank_score += damping_factor * rank_value_dict[neighbor] / len(graph.neighbors(neighbor))
            diff += abs(rank_score - rank_value_dict[node])
            rank_value_dict[node] = rank_score
        print "Iteration time(end): {}".format(time)
        if diff < min_delta:
            print "algorithm converge!"
            break
    print "pagerank algorithm calculate over!"
    return rank_value_dict


if __name__ == '__main__':
    pass
