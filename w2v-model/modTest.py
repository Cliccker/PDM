from gensim.models import Word2Vec

magazine = "压力容器"
model_file_name = '../Mod/' + magazine + '.model'
en_wiki_word2vec_model = Word2Vec.load(model_file_name)

testwords = ['有限元','封头','管道','应力']
for i in range(4):
    res = en_wiki_word2vec_model.most_similar(testwords[i])
    print(testwords[i])
    print(res)
