# coding:utf-8
import multiprocessing
import jieba
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time
import re

magazine = "压力容器"
def separate(magazine):
    dictPath = '../data/Dicts/' + magazine + '_dict.txt'
    sumPath = '../data/Summaries/' + magazine + '_summary.txt'
    procPath = '../data/Processed/' + magazine + '_proc.txt'

    jieba.load_userdict(dictPath)  # 为jieba导入用户字典
    stopwords = [line.strip() for line in open('stop_words.txt', encoding='UTF-8').readlines()]
    input_file = open(sumPath, 'r', encoding='utf-8')
    output_file = open(procPath, 'w', encoding='utf-8')
    lines = input_file.readlines()
    for line in lines:
        # 这里是为了去除所有英文字符
        sentence = jieba.cut(line.split('\n')[0].replace(' ', ''))
        # 输出结果为outstr
        outstr = ''
        # 去停用词
        for word in sentence:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        output_file.write(outstr)
    print('分词程序执行结束！')


if __name__ == "__main__":
    separate(magazine)

    input_file_name = '../data/Processed/' + magazine + '_proc.txt'
    model_file_name = '../Mod/' + magazine + '.model'

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
    model = Word2Vec(LineSentence(input_file_name),
                     size=400,  # 词向量长度为400
                     window=8,
                     min_count=5,
                     workers=multiprocessing.cpu_count(),
                     iter=10,
                     sg=1,
                     hs=1)

    model.save(model_file_name)
    end = time.process_time()  # 计时模块
    print('模型已保存!\n转换用时: %s Seconds' % (end - start))
