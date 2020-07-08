# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship
import collections


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        link = Graph("http://localhost:7474", username="neo4j", password="1234")
        self.graph = link
        # 定义label
        self.entity_name = '实体'
        self.entity_id = '编号'
        self.graph.delete_all()

    def create_node(self, nodeKey, nodeValue,nodeDict):
        """建立节点"""
        """建立标题节点"""
        for Key in nodeKey:
            name_node = Node(self.entity_name, name=Key)
            self.graph.create(name_node)
        """建立序号节点"""
        for name in nodeValue:
            id_node = Node(self.entity_id, name=name,title=nodeDict[name])
            self.graph.create(id_node)

    def create_relation(self, df_data,id_data,nodeDict,fullname_dict):
        """建立联系"""
        m = 0
        for m in range(0, len(df_data)):
            try:
                rel = Relationship(self.graph.find_one(label=self.entity_name, property_key='name',
                                                       property_value=df_data['itself'][m]),
                                   df_data['relation'][m],
                                   self.graph.find_one(label=self.entity_name, property_key='name',
                                                       property_value=fullname_dict[df_data['superior'][m]]))

                self.graph.create(rel)
            except AttributeError as e:
                print(e, m)
            except KeyError as ee:
                print(ee,m)
        n = 0
        for n in range(0, len(id_data)):
            try:
                rel = Relationship(self.graph.find_one(label=self.entity_id, property_key='name',
                                                           property_value=id_data['itself'][n]),
                                       df_data['relation'][n],
                                       self.graph.find_one(label=self.entity_id, property_key='name',
                                                           property_value=id_data['superior'][n]))

                self.graph.create(rel)
            except AttributeError as e:
                print(e, n)
            except KeyError as ee:
                print(ee, n)
