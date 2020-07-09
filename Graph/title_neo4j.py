# -*- coding: utf-8 -*-
from DataToNeo4jClass import DataToNeo4j
import pandas as pd

# 提取excel表格中数据，将其转换成Dataframe类型
standard_data = pd.read_excel('./Data/demo.xlsx', header=0, encoding='utf8')
print("Data Loaded")

def data_extraction():
    """节点数据抽取"""
    # 取出标题到list
    node_list_id = []
    nodeDict = {}
    for i in range(0, len(standard_data)):
        ID = standard_data['序号'][i]
        label = standard_data['类别'][i]
        title = standard_data['标题'][i]
        node_list_id.append([label, ID])
        nodeDict[ID] = [label, title]
    print("Node Extracted")
    return node_list_id, nodeDict


def relation_extraction():
    """联系数据抽取"""
    id_dict = {}
    relation_list = []
    id_list = []
    entity_list = []

    for i in range(0, len(standard_data)):
        m = 2
        id_node = standard_data[standard_data.columns[1]][i]  # 序号
        while m < len(standard_data.columns) - 1:
            relation_list.append(standard_data.columns[m + 1])  # 关系
            entity_list.append(standard_data[standard_data.columns[m + 1]][i])  # 关系实体
            id_list.append(id_node)
            m += 1

    id_dict['itself'] = id_list
    id_dict['relation'] = relation_list
    id_dict['superior'] = entity_list
    # 将数据转成DataFrame,去除空值
    id_data = pd.DataFrame(id_dict).dropna(axis=0, how='any').reset_index(drop=True)
    print("Relation Extracted")
    return id_data


create_data = DataToNeo4j()
Da = data_extraction()
Re = relation_extraction()
create_data.create_node(Da[0], Da[1])
create_data.create_relation(Re, Da[1])
print("FINISHED")
