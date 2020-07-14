import pandas as pd


def text_save(filename):  # filename为写入CSV文件的路径，data为要写入数据列表.
    data = []
    corpus = pd.read_csv('dictList.csv')
    corpus = corpus.values.tolist()
    for i in range(len(corpus)):
        data.append(corpus[i][1])
    file = open(filename, 'w',encoding='utf-8')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


text_save('D:\文件\文献\我的坚果云\学习\python学习进度\word2vec\jieba_dict.txt')
