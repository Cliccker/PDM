# -*- coding: utf-8 -*-
from DataToNeo4jClass import DataToNeo4j
import pandas as pd

# 提取excel表格中数据，将其转换成dateframe类型
standard_data = pd.read_excel('./Data/demo.xlsx', header=0, encoding='utf8')
print(standard_data)


def data_extraction():
    """节点数据抽取"""

    # 取出标题到list
    node_list_id = []
    node_list_value = []
    fullname_dict ={}
    nodeDict = {}
    for i in range(0, len(standard_data)):
        id = standard_data['序号'][i]
        title = standard_data['标题'][i]
        node_list_id.append(id)
        node_list_value.append(title + "_" + id)
        fullname_dict[id] = title + "_" + id
        print(fullname_dict)
        fullname_dict['ASME'] = "ASME标准"
        nodeDict[id] = title
        nodeDict['ASME'] = "ASME标准"

    return node_list_value, node_list_id, nodeDict, fullname_dict


"""
    # value抽出作node
    node_list_value = []
    for i in range(0, len(standard_data)):
        for n in range(1, len(standard_data.columns)):
            # 取出表头名称
            node_list_value.append(standard_data[standard_data.columns[n]][i])
    node_list_value = list(set(node_list_value))
    node_list_value = [incom for incom in node_list_value if str(incom) != 'nan']  # 去除空值
"""


def relation_extraction():
    """联系数据抽取"""
    links_dict = {}
    id_dict = {}

    relation_list = []
    id_list = []
    title_list = []
    entity_list = []

    for i in range(0, len(standard_data)):
        m = 1
        n = 0
        name_node = standard_data[standard_data.columns[m]][i]
        id_node = standard_data[standard_data.columns[n]][i]
        while m < len(standard_data.columns) - 1:
            relation_list.append(standard_data.columns[m + 1])
            entity_list.append(standard_data[standard_data.columns[m + 1]][i])
            title_list.append(name_node + '_' + id_node)
            id_list.append(id_node)
            m += 1
            n += 1

    # 整合数据，将两个list整合成一个dict
    links_dict['itself'] = title_list
    links_dict['relation'] = relation_list
    links_dict['superior'] = entity_list
    
    id_dict['itself'] = id_list
    id_dict['relation'] = relation_list
    id_dict['superior'] = entity_list
    # 将数据转成DataFrame
    df_data = pd.DataFrame(links_dict).dropna(axis=0, how='any').reset_index(drop=True)
    id_data = pd.DataFrame(id_dict).dropna(axis=0, how='any').reset_index(drop=True)

    return df_data, id_data


create_data = DataToNeo4j()
Da = data_extraction()
Re = relation_extraction()
create_data.create_node(Da[0], Da[1],Da[2])
create_data.create_relation(Re[0], Re[1], Da[2],Da[3])
print("finished")
