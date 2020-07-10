# -*- coding: utf-8 -*-
from py2neo import Node, Graph, Relationship


class DataToNeo4j(object):
    """将excel中数据存入neo4j"""

    def __init__(self):
        """建立连接"""
        link = Graph("http://localhost:7474", username="neo4j", password="1234")
        self.graph = link
        self.graph.delete_all()

    def create_node(self, nodeValue, nodeDict):
        """建立序号节点"""
        n = 0
        for name in nodeValue:
            id_node = Node(name[0], title=name[1], name=nodeDict[name[1]][1])
            self.graph.create(id_node)
            n += 1
        print("{} Nodes Created".format(n))

    def create_relation(self, id_data, nodeDict):
        """建立联系"""
        count = 0
        for n in range(0, len(id_data)):
            try:
                rel = Relationship(self.graph.find_one(label=nodeDict[id_data['itself'][n]][0], property_key='title',
                                                       property_value=id_data['itself'][n]),
                                   id_data['relation'][n],
                                   self.graph.find_one(label=nodeDict[id_data['superior'][n]][0], property_key='title',
                                                       property_value=id_data['superior'][n]))
                self.graph.create(rel)
                count += 1
            except AttributeError as e:
                print(e, n)
            except KeyError :
                pass
        print("{} Relationships Created".format(count))
