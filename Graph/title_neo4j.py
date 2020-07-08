# -*- coding: utf-8 -*-
from DataToNeo4jClass import DataToNeo4j
from py2neo import Node, Graph, Relationship
import os
import pandas as pd


# 提取excel表格中数据，将其转换成dateframe类型

standard_data = pd.read_excel('./Data/demo.xlsx', header=0, encoding='utf8')
print(standard_data)


def data_extraction():
    """节点数据抽取"""

    # 取出标题到list
    node_list_id = []
    nodeDict = {}
    for i in range(0, len(standard_data)):
        node_list_id.append(standard_data['序号'][i])
        nodeDict[standard_data['序号'][i]] = standard_data['标题'][i]

    # value抽出作node
    node_list_value = []
    for i in range(0, len(standard_data)):
        for n in range(1, len(standard_data.columns)):
            # 取出表头名称
            node_list_value.append(standard_data[standard_data.columns[n]][i])
    node_list_value = list(set(node_list_value))
    return  node_list_value ,node_list_id,nodeDict


def relation_extraction():
    """联系数据抽取"""
    links_dict ={}
    id_list = []
    entity_list = []

    for i in range(0, len(standard_data)):
        m = 1
        name_node = standard_data[standard_data.columns[m]][i]
        while m < len(standard_data.columns)-1:
            entity_list.append(standard_data[standard_data.columns[m + 1]][i])
            id_list.append(name_node)
            m += 1


    # 整合数据，将两个list整合成一个dict
    links_dict['itself'] = id_list
    links_dict['superior'] = entity_list
    # 将数据转成DataFrame
    df_data = pd.DataFrame(links_dict)
    return df_data
print(data_extraction())
print(relation_extraction())
create_data = DataToNeo4j()
create_data.create_node(data_extraction()[0], data_extraction()[1],data_extraction()[2])
create_data.create_relation(relation_extraction())
"""
# 实例化对象
data_extraction()
relation_extraction()




"""
