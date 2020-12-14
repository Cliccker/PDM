from gensim.models import Word2Vec

magazine = "FEA"
model_file_name = '../Mod/' + magazine + '.model'
word2vec_model = Word2Vec.load(model_file_name)


def similarwords(word):
    req_count =10
    print(word)
    for key in word2vec_model.wv.similar_by_word(word, topn=100):

        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;


test_pair = [["有限元分析", "有限元"], ["有限元分析", "分析"],
             ["应力分析", "强度分析"], ["应力分析", "应力"],
             ["压力", "内压"], ["压力", "外压"], ["压力", "温度"]]
for [i, j] in test_pair:
    print(word2vec_model.wv.similarity(i, j))


word_list = ["有限元分析", "应力", "压力", "法兰", "封头", "压力容器"]

for word in word_list:
    similarwords(word)
