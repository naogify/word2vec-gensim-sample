import MeCab

# -F：出力形式を指定 （ \\\s%f[6]: で単語間を半角スペースで区切る）
# -U：未知語の出力形式を設定
# -E：解析結果の終端に表示する文字を指定する。（ \\\n: で改行コードを追加）
# 参考: http://www.mwsoft.jp/programming/munou/mecab_command.html#node-format

tagger = MeCab.Tagger('-r /etc/mecabrc -F \\\s%f[6] -U%m -E \\\n')
with open("kokoro.txt", "r", encoding="shift-jis") as f:
    text = f.readlines()
    for line in text:
        if "。" in line:
            result = tagger.parse(line)
            with open("kokoro_wakati.txt", "a", encoding="utf-8") as of:
                of.write(result[1:])
        else:
            pass
print("Finish")