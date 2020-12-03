# -*- coding: utf-8 -*-
# @Time ： 2020/12/3 9:33
# @Auth ： Cheng
# @File ：聚合论文.py
# @IDE ：PyCharm

# -*- coding: utf-8 -*-
import os

base_path = r'Paper'
files = os.listdir(base_path)
all_papers = open("论文聚合.txt", "w", encoding="utf-8")
for path in files:
	full_path = os.path.join(base_path, path)
	with open(full_path, encoding="utf-8") as fp:
		data = fp.read()
		all_papers.write(data)
