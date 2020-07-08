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
        self.entity_name = ["一级标题","二级标题","三级标题","四级标题",]
        self.entity_id = '编号'
        self.graph.delete_all()

    def create_node(self, nodeKey, nodeValue, nodeDict):
        """建立节点"""
        for key in nodeDict:
            print(key)
            Zero = collections.Counter(key)
            print(Zero['0'])
            if Zero['0'] == 0:
                name_node = Node(self.entity_name[3], name=nodeDict[key])
                self.graph.create(name_node)
            if Zero['0'] == 1:
                name_node = Node(self.entity_name[2], name=nodeDict[key])
                self.graph.create(name_node)
            if Zero['0'] == 2:
                name_node = Node(self.entity_name[1], name=nodeDict[key])
                self.graph.create(name_node)
            if Zero['0'] == 3:
                name_node = Node(self.entity_name[0], name=nodeDict[key])
                self.graph.create(name_node)

        for name in nodeValue:
            id_node = Node(self.entity_id, name=name)
            self.graph.create(id_node)

    def create_relation(self, df_data):
        """建立联系"""

        m = 0
        for m in range(0, len(df_data)):
            i = 3
            while i >0:
                try:
                    rel = Relationship(self.graph.find_one(label=self.entity_name[i], property_key='name',
                                                           property_value=df_data['itself'][m]),
                                       '属于',
                                       self.graph.find_one(label=self.entity_name[i-1], property_key='name',
                                                           property_value=df_data['superior'][m]))
                    self.graph.create(rel)

                except AttributeError:
                    pass
                i -=1 