#!/usr/bin/env python3
# coding: utf-8

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 少しよし'
omikuji_4 = '吉 よし'
omikuji_5 = '凶 わるし'

# fortuneにomiku_1を代入
unsei = omikuji_1

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')