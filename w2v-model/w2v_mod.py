# coding:utf-8
import multiprocessing
import jieba
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

'''
magazine 杂志名，可以更换成多本杂志的合集或者别的数据库
dictPath 字典文件
sumPath 未分词的摘要文件
procPath 去除英文和数字并分词完成摘要文件
modPath 词向量模型文件
'''

magazine = "压力容器"
dictPath = '../data/Dicts/' + magazine + '_dict.txt'
sumPath = '../data/Clean/' + magazine + '_summary.txt'
# sumPath = 'data/Clean/所有语料.txt'
procPath = '../data/Processed/' + magazine + '_proc.txt'
# modPath = '../Mod/' + magazine + '.model'
modPath = '../Mod/FEA_2.model'


def separate():
    jieba.load_userdict(dictPath)  # 为jieba导入用户字典
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]  # 去除停用词
    input_file = open(sumPath, 'r', encoding='utf-8')
    output_file = open(procPath, 'w', encoding='utf-8')
    lines = input_file.readlines()
    for line in lines:
        sentence = jieba.cut(line.split('\n')[0].replace(' ', ''))
        # 输出结果为outputStr
        outputStr = ''
        # 去停用词
        for word in sentence:
            if word not in stopwords:
                if word != '\t':
                    outputStr += word
                    outputStr += " "
        output_file.write(outputStr+'\n')
    print('分词程序执行结束！')


if __name__ == "__main__":
    separate()
    '''
     LineSentence(inp)：格式简单：一句话=一行; 单词已经过预处理并被空格分隔。
     size：是每个词的向量维度； 
     window：是词向量训练时的上下文扫描窗口大小，窗口为5就是考虑前5个词和后5个词； 
     min-count：设置最低频率，默认是5，如果一个词语在文档中出现的次数小于5，那么就会丢弃； 
     workers：是训练的进程数（需要更精准的解释，请指正），默认是当前运行机器的处理器核数。这些参数先记住就可以了。
     sg ({0, 1}, optional) – 模型的训练算法: 1: skip-gram; 0: CBOW
     alpha (float, optional) – 初始学习率
     iter (int, optional) – 迭代次数，默认为5
     '''
    print('开始转换...')
    start = time.process_time()
    model = Word2Vec(LineSentence(procPath),
                     size=10,  # 词向量长度为400
                     window=3,
                     min_count=3,
                     workers=multiprocessing.cpu_count(),
                     iter=20,
                     sg=0,
                     hs=1)

    model.save(modPath)
    end = time.process_time()  # 计时模块
    print('模型已保存!\n转换用时: %s Seconds' % (end - start))
