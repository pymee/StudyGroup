#!/usr/bin/env python3
# coding: utf-8

# typeや追加、削除、特定の要素の確認については、インタプリタで確認。

# モジュールをインポート
import random

omikuji = {'運勢1': '大吉 すべてよし',
           '運勢2': '中吉 まあまあよし',
           '運勢3': '吉 よし',
           '運勢4': '凶 わるし'
}

#辞書(omikuji)のValue(値)をoutput_omikujiに代入
output_omikuji = omikuji.values()

# output_omikujiをrandom.choiceした結果をunseiに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei = random.choice(list(output_omikuji))

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')