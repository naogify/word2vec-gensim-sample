from gensim.models import word2vec
docs = word2vec.LineSentence("kokoro_wakati.txt")
# オプション一覧
# https://qiita.com/dskst/items/a9571bdd74a30a5e8d55
model = word2vec.Word2Vec(docs,
                        size=100,
                        min_count=5,
                        window=5,
                        iter=3)
model.save("kokoro.model")