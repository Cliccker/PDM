from gensim.models import Word2Vec

magazine = "压力容器"
model_file_name = '../Mod/' + magazine + '.model'
word2vec_model = Word2Vec.load(model_file_name)
'''
test_pair = [["有限元分析", "有限元"], ["有限元分析", "分析"],
             ["应力分析", "强度分析"], ["应力分析", "应力"],
             ["压力", "内压"], ["压力", "外压"], ["压力", "温度"]]
for [i, j] in test_pair:
    print(en_wiki_word2vec_model.wv.similarity(i, j))
'''
req_count = 10
for key in word2vec_model.wv.similar_by_word("超高压容器", topn=100):
    if len(key[0]) == 3:
        req_count -= 1
        print(key[0], key[1])
        if req_count == 0:
            break;
