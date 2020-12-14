# -*- coding: utf-8 -*-
# @Time ： 2020/12/13 19:51
# @Auth ： Cheng
# @File ：visualization.py
# @IDE ：PyCharm

from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
from pylab import *
from sklearn.manifold import TSNE

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

magazine = "FEA_2"
model_file_name = '../Mod/' + magazine + '.model'
word2vec_model = Word2Vec.load(model_file_name)

X = word2vec_model.wv[word2vec_model.wv.vocab]
pca = PCA(n_components=2)
result = TSNE(n_components=2, learning_rate=100).fit_transform(X)
# 可视化展示

plt.figure(figsize=(20, 6.5))
words = ["有限元", "有限元分析", "有限元计算",
         "压力", "温度", "大气压", "力矩",
         "螺栓", "整体法兰", "法兰结构", "法兰",
         "压力容器", "超高压容器", "承压设备", "压力容器标准", "高压容器", "压力管道"
         ]
for i, word in enumerate(words):
	pyplot.scatter(result[i, 0], result[i, 1], c="blue", s=10)
	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))

# words_2 = ["压力", "温度", "压差", "大气压", "力矩"]
# for i, word in enumerate(words_2):
# 	pyplot.scatter(result[i, 0], result[i, 1], c="green", s=10)
# 	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
