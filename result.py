# 標準出力（ターミナル）をut-f8に指定する。デバッグ用。
# https://hodalog.com/about-unicodeencodeerror-using-japanese-in-python-code/
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from gensim.models import word2vec
model   = word2vec.Word2Vec.load("kokoro.model")
results = model.most_similar(positive="先生", topn=10)
for result in results:
    print(result[0], '\t', result[1])