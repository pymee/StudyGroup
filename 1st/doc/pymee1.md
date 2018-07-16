<!-- page_number: true -->

# 第1回 Pymee

---

# 事前準備確認

+ Pythonのインストール
+ 勉強資料のダウンロード

---

# はじめに

+ Pymeeとは？
	+ Python metting
	+ Pythonで何かしよう！
	+ 今年度はPython勉強会を企画
+ メンバー紹介

---
# 勉強会について
+ ゴール
	+ 自分でプログラムを作れるようになる
+ どうやって
	+ おみくじプログラムを全3回の勉強会で作成
	+ プログラム作成を通してpythonの知識をつける

---

# 勉強会の予定
+ 2018/8/22 第１回目
	+ おみくじプログラムを通して基本的な文法学習
+ 2018/11下旬
	+ おみくじプログラムを通してファイルの入出力
+ 2019/2下旬
	+ おみくじプログラムとDBを連携させる

---

# 今日の内容

+ プログラミングって？
+ 実際のプログラムを書いてみよう！
+ おみくじの種類を増やそう
+ 名前を入力しよう
+ 自動で結果を出力しよう
+ もっと短くしてみよう
+ 違う方法でやってみよう
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---
# プログラミングって？
+ コンピュータにやってもらい処理を書いて指示する事
+ 指示内容について書いたものが「プログラム」
+ インタプリタ
	+ 指示内容を機械がわかるような形で翻訳する

---
# Pythonって？
+ 指示内容の記載に使用する言葉
+ プログラミング言語の一種
---
# 実際にプログラムを書いてみよう
+ 作るプログラム
	+ プログラムを実行
	+ 「あなたの運勢は、大吉 すべてよし」と出力される
---
# やり方
1. 勉強用フォルダを作成
3. 勉強会用フォルダにテキストファイル「01_print.py」を作成
4. 下記内容を入力
```
#!/usr/bin/env python3
# coding: utf-8

# printは()の中身を表示してくれます。
print('あなたの運勢は、大吉 すべてよし')
```
5. プログラムの実行
```
$ python test.py 
```
6. 「あなたの運勢は、大吉 すべてよし」と出力されることを確認
---
# プログラムの実行
プログラムの実行方法は下記の通りです
+ 処理内容を書いたファイルを作成
+ ターミナル、コマンドプロンプトで下記コマンドを実行
```
python ファイル名
```
作成したプログラムが実行されます
実際に作成したファイルを開いて内容を確認します

---
# #!/usr/bin/env python3とは？
+ Shebang(シェバン、シバン)
	+ 「#!」で始めてその後にパスを記載する
+ インタプリタの絶対パス
	 + Python2,3の使い分けが可能
	 Python2,3は互換性がない、基本的にPython3を使用する
+ Unix/系のプラットフォームで使用、windowsは記載する必要がない
+ 次スライドの方法でプログラムを実行する場合は必要

---
# プログラムの実行(発展系)
0. ファイル名.pyのプログラムを作成する
1. 所有者に実行権限付与する
```
$ chmod 744 test.py
```
2. プログラムの実行(ファイル名のフルパスを指定する必要あり)
```
$ ./test.py 
```
---
# # coding: utf-8
+ プログラムファイルの文字コードを指定している
	+ python3はデフォルトが「UTF-8」
	+ python2はデフォルトが「ASCII」

---
# コメント文
+ 先頭が「#」で始まる文
+ プログラム実行時に無視される
+ プログラムの内容を補足する

---
# 文字、値を出力する

> print('出力する文字')

（）内の中身を表示する
文字列を出力するには「'」か「"」で囲む必要がある

「'」か「"」で囲まないとエラーが出力され実行がうまくいかない

```
$ python 01_print.py
File "01_print.py", line 4
 print(あなたの運勢は、大吉すべてよし)
                        ^
SyntaxError: invalid character in identifier
```
---
# 関数
+ 関数とは？
	+ print()は関数
	+ 特定の機能(与えた文字を出力する)を持つプログラムの塊
	+ 「print」が関数名
	+ ()の中に記述するものを「引数(ひきすう)」という
	+ 関数を実行した際に、戻る値を「戻り値」という
+ 組み込み関数
	+ 元から使えるようになっている関数
---

# データ型とは？
扱うデータの種類
+ 文字列(こんにちは、名前、pymee)
+ 数値(1, 100, 80)
+ 浮動小数点数(1.09, 20.59)
+ Bool(True, False)

Pythonでは自動で判別のため、データ型の宣言は不要

---
# 型ではデータをしまう箱
> print('あなたの運勢は、大吉すべてよし')

'あなたの運勢は、大吉すべてよし'の型は**文字列**
箱(オブジェクト)を作成して文字列を格納している

---
# 型の種類を確認する
> type(確認する値)
値の型を確認することができる
+ プログラムの内容
```
#!/usr/bin/env python3
#coding: utf-8

print("あなたの運勢は、大吉すべてよし")
print(type("あなたの運勢は、大吉すべてよし"))
```
+ 出力結果
'str'は文字列のこと
```
$ python 01_print.py
あなたの運勢は、大吉すべてよし
<class 'str'>
```
---
# まとめ
+ プログラミングって？
	+ コンピュータにやってもらいたいことを書いて実行する
	+ 処理を書いた言語のことをプログラミング言語→Python
+ プログラムの実行までの流れ
	+ 処理内容を書いた「ファイル名.py」を作成
	+ 「python ファイル名.py」で実行
+ 型って？
	+ 型をしまう箱の種類

---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ おみくじの種類を増やそう
+ 名前を入力しよう
+ 自動で結果を出力しよう
+ もっと短くしてみよう
+ 違う方法でやってみよう
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---
# おみくじの種類を増やそう
+ １種類を５種類にしよう！

大吉 すべてよし
中吉 まあまあよし
小吉 よし
吉 すこしよし
凶 わるし

---
# どうやって？

今までのプログラム
```
#!/usr/bin/env python3
#coding: utf-8

print("あなたの運勢は、大吉すべてよし")
```
printの中身を5つ分書き換えるのは手間...
**変数**を使用する！

---
# 変数とは？
+ 値が入っている箱につけたラベル
+ 箱のラベル、つまり変数を指定することで中身であるデータを取り出すことができる
	+ print(変数) を実行すると、変数の中身が出力される
---
# 変数の定義
> 変数名 = 値

上記の形で変数とそれに格納する値を定義することが可能
変数名に使用可能な文字は下記の通り

変数「omikuji_1」に「'大吉 すべてよし'」という値を格納している
```
omikuji_1 = '大吉 すべてよし'
```
---
# 変数の定義の注意事項
+ 使用可能な文字
	+ 小文字の英字(a-z)
	+ 大文字の英字(A-Z)
	+ 数字(0-9)
	+ アンダースコア(_)
+ 先頭が数字、もしくはアンダースコアは使えない
+ 特定の単語はすでに予約されており使えない
	+ Flase, classなど
---
# print(omikuji_1)の流れ
箱のラベルが「omikuji_1」のものを見つける
print()が箱の中身を出力する

---
# 文字列と変数の組み合わせ
+ 文字列と変数を組み合わせるには「+」を使用する
---
# インタプリタの対話モードで動作確認をしてみよう！
+ 対話モードとは？
	+ コードを読み取りつつ、実行することが可能
+ 使い方
	+ 「python3.6」と入力
	+ プロンプトが「>>>」となることを確認
	+ そのまま実施したい処理を入力する
	+ 対話モードを終了するときは「Ctrl」と「D」を同時に押下、もしくは「quit()」と入力
---

# 対話モードで動作確認をしてみよう！
変数の定義を対話モードを使用してやってみよう
1. インタプリタの対話モードを起動し、「>>>」が出力されることを確認

<font style = "font-size: 80%">

```
$ python3.6
Python 3.6.5 (default, May  4 2018, 21:19:29) 
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

</font>

---

# 対話モードで動作確認をしてみよう！

2. 変数の定義
変数名 = 値 の形で定義
```
>>> omikuji_1 = '大吉 すべてよし'
```
3. 変数の中身を確認
変数名を入力して値を確認する
```
>>> omikuji_1
'大吉 すべてよし'
```
---
# 対話モードで動作確認をしてみよう！
変数をprint()を使用して出力してみる
```
>>> print(omikuji_1)
大吉 すべてよし 
```
「大吉 すべてよし 」を出力されることを確認する
このように変数を使用して値を扱うことができる

---

# 入力
> input(実行時に表示する値)

コマンドプロンプトやコンソールに入力された値を受け取る

> 変数 = input()

受け取った値を変数に格納することが可能

---
# 対話モードで動作確認をしてみよう！
自分の名前を入力して出力しよう
1. インタプリタの対話モードを起動し下記を入力
実行時に「>>」が出力されるので、名前を入力する
```
>>> name = input('>>')
>> 名前　※自分で入力する
```
2. 変数「name」の中身を確認
変数名「name」を入力、もしくはpirnt(name)を実行して入力した名前が表示されることを確認
```
>>> name
'名前'
>>> 
>>> print(name)
名前
```

---
# おみくじプログラムを改良しよう！
1. おみくじの種類を５種類にする
2. おみくじを引く人の名前を入力する

---
# おみくじプログラムを改良しよう！
1. ファイル「01_print.py」をコピーして「02_variable.py」に変更
2. 「#coding: utf-8」の下に５種類のおみくじをそれぞれ変数に格納
**コメント文(#から始まる部分)は記載不要です**
```
#!/usr/bin/env python3
# coding: utf-8

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_5 = '凶 わるし'
```
3. 出力用の変数「unsei」に出力させたいおみくじの変数を代入
```
# unseiにomikuji_1を代入
unsei = omikuji_1
```
---
# おみくじプログラムを改良しよう！
4. おみくじを引く人の名前の入力を促すメッセージを出力させます
```
print('あなたの名前を入力してください')
```
5. 入力された文字列を変数「name」に代入します
input実行時に「>>」を出力
```
# 名前を入力
name = input('>>')
```
---
# おみくじプログラムを改良しよう！
6. 最後におみくじ結果の部分を修正します
変数と文字列を組み合わせておみくじを引いた結果を出力させます
+ 修正前
```
# printは()の中身を表示してくれます。
print('あなたの運勢は、大吉 すべてよし')
```
+ 修正後
```
# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```
---
# 完成コード
```
#!/usr/bin/env python3
# coding: utf-8

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_5 = '凶 わるし'

# unseiにomikuji_1を代入
unsei = omikuji_1

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```
---
# まとめ
+ 変数とは？
	+ 値が格納する箱のラベル
+ 変数と文字列を一緒に出力するには？
	+ print(変数 + '文字列')で出力可能
+ 入力するには？
	+ input()を使用する

---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ ~~おみくじの種類を増やそう~~
+ ~~名前を入力しよう~~
+ 自動で結果を出力しよう
+ もっと短くしてみよう
+ 違う方法でやってみよう
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---
# 自動で結果を出力しよう
前回までのプログラムでは特定のおみくじを選んで出力していた
(大吉だけしか出ないようなおみくじに！)

このままでは、神主さんが誰かがプログラムを実行するたびに出力するおみくじの中身を書き換えないといけないことに！(運用でカバーというやつですね)

なので、任意のおみくじが出力されるようにプログラムを改良しよう！

---
# どうやって？
+ 0-4の数字から任意の数字を選ぶ
+ 選んだ数字によって出力するおみくじの内容を変える
例) もし数字が「0」だったら「大吉 すべてよし」を出力

	| 数字 | おみくじ結果 |
	|:---:|:---|
	| 0 | 大吉 すべてよし |
	| 1 | 中吉 まあまあよし |
	| 2 | 小吉 よし |
	| 3 | 吉 すこしよし |
	| 4 | 凶 わるし |

---
# 0-4の数字から任意の数字を選ぶ
> import random
> random.randrange(start, stop[, step])

startやstop、stepには整数を記載
start以上end未満の整数から任意の整数を選択する
step部分は増減部分を示しており、記載しなくても問題なし
「import random」を定義しないと使えない

+ 0-4(５未満なので)の整数から任意の数を選択している
```
>>> import random
>>> random.randrange(0,5)
1
>>> random.randrange(0,5)
4
>>> random.randrange(0,5)
3
```
---

# 選んだ数字によって出力するおみくじの内容を変える

**もし**数字が「0」**だったら**(条件)、「大吉 すべてよし」を出力(処理)
+ 条件分岐
もし、条件1だったら、処理1を行う
```
if 条件１:
	処理１
```
---
# 条件分岐
```
if 条件1:
	処理1
elif 条件2:
	処理2-1
    処理2-2
else:
	処理3
```
1. もし、条件1に一致した場合は、処理1を実行
1. 条件1に一致せず、条件2に一致した場合は、処理2-1,2-2を実行
1. 条件1、条件2のどちらにも一致しなかった場合は、処理3を実行
+ 処理の部分は先頭にスペースを4つ入力する必要がある、処理が１行以上ある場合は全てについて先頭にスペース4つをつける
+ elifの条件から処理、elseの条件から処理の部分は必須ではない
---

# 条件部分の記述
+ 比較演算子を使用する

| 条件 | 演算子 | 使用例 | 使用例意味|
|---|:---:|:---:|---|
| と等しい| == | x == 1| xが１と等しい |
| と等しくない| != | x != 1| xが１と等しくない |
| より小さい| < | x < 1| xが１より小さい |
| 以下| <= | x <= 1| xが１以下 |
| より大きい| > | x > 1| xが１より大きい |
| 以上| >= | x >= 1| xが１以上|
| 要素になっている| in | x in 1| xに1が含まれている|

---
# 対話モードで動作確認をしてみよう！
変数「unsei」が「0」だった場合、「大吉」
変数「unsei」が「1」だった場合、「吉」
変数「unsei」がそれ以外の場合、「該当なし」と表示する

1. インタプリタの対話モードを起動
```
$ python3.6
```
2. 変数「unsei」を定義する、値は0-2の任意の値を代入
```
>>> unsei = 1
```
---
# 対話モードで動作確認をしてみよう！
3. if文を作成し変数の値を元に出力する値を変える
「2」で代入した値によって、出力される値が変わる
下記は、変数「unsei」に「1」が代入されていたため「吉」が出力
```
>>> if unsei == 0:
...     print("大吉")
... elif unsei == 1:
...     print("吉")
... else:
...     print("該当なし")
... 
吉
```
---
# おみくじプログラムを改良しよう！
1. 0-4の数字から任意の数字を選ぶ
	+ random.randrange(0, 5)で0−4から任意の整数を選択し変数「num」に代入 
2. 選んだ数字によって出力するおみくじの内容を変える
	+ 条件分岐の内容

	| 条件(numが〜だったら) | 処理(変数「unsei」に〜を代入) |
	|:---:|---|
	| 0 | 大吉 すべてよし |
	| 1 | 中吉 まあまあよし |
	| 2 | 小吉 よし |
	| 3 | 吉 すこしよし |
	| 4 | 凶 わるし |

---

# 0-4の数字から任意の数字を選ぶ
1. ファイル「02_variable.py」をコピーし、ファイル名を「03_ransu_if.py」にする
2. 「# coding: utf-8」の次に、「import random」を追加
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random
```

---

# 0-4の数字から任意の数字を選ぶ
3. 変数の下に、「random.randrange()」を追加

<font style = "font-size: 80%">
  
```
# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_5 = '凶 わるし'

# random.randrangeは()の中の数字からランダムで数字を選択してくれます
# 選択した数字をnumに代入
num = random.randrange(0,6)
```
</font>

---

# 0-4の数字から任意の数字を選ぶ
4. 「3」の下に条件分岐を追加
```
# numに格納された数字によって出力される文字列を変更
if num == 0:
	unsei = omikuji_1
elif num == 1:
	unsei = omikuji_2
elif num == 2:
	unsei = omikuji_3
elif num == 3:
	unsei = omikuji_4
elif num == 4:
	unsei = omikuji_5
else:
	unsei = ""
```

---

# 完成コード(1/3)
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_5 = '凶 わるし'

# random.randrangeは()の中の数字からランダムで数字を選択してくれます
# 選択した数字をnumに代入
num = random.randrange(0,6)
```

---

# 完成コード(2/3)
```
# numに格納された数字によって出力される文字列を変更
if num == 0:
	unsei = omikuji_1
elif num == 1:
	unsei = omikuji_2
elif num == 2:
	unsei = omikuji_3
elif num == 3:
	unsei = omikuji_4
elif num == 4:
	unsei = omikuji_5
else:
	unsei = ""
```

---

# 完成コード(3/3)
```
print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```

---

# まとめ
+ 条件分岐
	+ もし条件だったら処理を行う
	+ 条件は比較演算子を使用して記述
```
if 条件1:
	処理1
elif 条件2:
	処理2
else:
	処理3
```

---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ ~~おみくじの種類を増やそう~~
+ ~~名前を入力しよう~~
+ ~~自動で結果を出力しよう~~
+ もっと短くしてみよう
+ 違う方法でやってみよう
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---

# もっと短くしてみよう
+ おみくじの数を増やす場合、下記3つの修正が必要
	1. 変数を定義
	2. random.randrange(0, 5)の部分を修正
	3. if文のelifを追加

+ もっとプログラムをシンプルなものにしよう！
+ そのために、**リスト**を使用する

---

# リストとは？
+ 今まで、箱を1つづつ用意し、その中に値を代入
+ リストの場合、これらの箱を1つの大きな箱にまとめる

---

# リストとは？
+ 大きな箱の中身は0から始まる番号が振られており、こちらを元に値を取り出すことが可能

---

# 対話モードで動作確認をしてみよう！

+ リストの定義
> リスト名 = [値, 値, 値...]

```
>>> omikuji = ['大吉', '小吉', '吉', '吉']
```
+ リスト名を入力して中身を確認
```
>>> omikuji
['大吉', '小吉', '吉', '吉']
```

---

# 対話モードで動作確認をしてみよう！
+ 値の取り出し
> リスト名[offset]
```
>>> omikuji[0]
'大吉'
>>> omikuji[1]
'小吉'
```
+ 下記のようにオフセットを範囲で指定することも可能(スライス)
```
>>> omikuji[0:3]
['大吉', '中吉', '小吉']
```

---

# 対話モードで動作確認をしてみよう！
+ 任意の場所へ追加
> リスト名.insert(offset, value)
+ 「大吉」の横に「中吉」を追加する
offsetは「0」から数える
```
>>> omikuji
['大吉', '小吉', '吉', '吉']
>>> 
>>> omikuji.insert(1, '中吉')
>>> 
>>> omikuji
['大吉', '中吉', '小吉', '吉', '吉'
```
---

# 対話モードで動作確認をしてみよう！
+ 値の削除
	+ offsetを指定しての削除
	> del リスト名[offset]
	「吉」を1つ削除する
	```
	>>> omikuji
	['大吉', '中吉', '小吉', '吉', '吉'
	>>> 
	>>> del omikuji[3]
	>>> 
	>>> omikuji
	['大吉', '中吉', '小吉', '吉']
	```
    
---

# 対話モードで動作確認をしてみよう！
+ 値の削除
	+ 値を元に削除 
	> リスト名.remove(値)
	```
	>>> omikuji
	['大吉', '中吉', '小吉', '吉', '吉']
	>>> 
	>>> omikuji.remove('吉')
	>>> 
	>>> omikuji
	['大吉', '中吉', '小吉', '吉']
	```
    + offsetが不明の時に便利
---
# 対話モードで動作確認をしてみよう！
+ 最後に値の追加
> リスト名.append(値)
```
>>> omikuji
['大吉', '中吉', '小吉', '吉']
>>> 
>>> omikuji.append('きょう')
>>> 
>>> omikuji
['大吉', '中吉', '小吉', '吉', 'きょう']
```
---
# 対話モードで動作確認をしてみよう！
+ 値の書き換え
> リスト名[offset] = 値
```
>>> omikuji
['大吉', '中吉', '小吉', '吉', 'きょう']
>>> 
>>> omikuji[4] = '凶'
>>> 
>>> omikuji
['大吉', '中吉', '小吉', '吉', '凶']
```
---
# おみくじプログラムを改良しよう
+ 5つの変数を1つのリストにまとめる
	+ 変数を5つ準備しなくても、1つで問題ない
+ ifの部分にリストを使用する
	+ random.randrange()で選んだ数字をリストのoffsetを使用する

---
# 5つの変数を1つのリストにまとめる
1. ファイル「03_ransu_if.py」をコピーし、ファイル名を「04-1_list.py」にする
2. ファイル名「04-1_list.py」を開く
---
# 5つの変数を1つのリストにまとめる
4. 変数部分をリストに書き換える
+ 削除部分
```
# 代入
omikuji_1 = '大吉 すべてよし'
omikuji_2 = '中吉 まあまあよし'
omikuji_3 = '小吉 よし'
omikuji_4 = '吉 すこしよし'
omikuji_5 = '凶 わるし'
```
+ 追加部分
```
# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
           '中吉 まあまあよし',
           '小吉 よし',
           '吉 すこしよし',
           '凶 わるし',
           ]
```
---
# ifの部分にリストを使用する
+ 削除部分
```
# numに格納された数字によって出力される文字列を変更
if num == 0:
	unsei = omikuji_1
elif num == 1:
	unsei = omikuji_2
elif num == 2:
	unsei = omikuji_3
elif num == 3:
	unsei = omikuji_4
elif num == 4:
	unsei = omikuji_5
else:
	unsei = ""
```
+ 追加部分
```
# omikuji[num]をunseiに代入
unsei = omikuji[num]
```
---
# 完成コード(1/2)
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
           '中吉 まあまあよし',
           '小吉 よし',
           '吉 すこしよし',
           '凶 わるし',
           ]
# 乱数を生成
num = random.randrange(0,5)
```

---
# 完成コード(2/2)
```

# omikuji[num]をunseiに代入
unsei = omikuji[num]

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```
---
# もっと短くしよう！
+ なぜ短い方がいいのか？
  **プログラムは書く時間より読む時間の方が長い**

+ 基本的には、短くてシンプルな方が後から読みやすい
+ 他人が後から読んでもわかりやすいようにコメントを入れたり、変数名をわかりやすくするように心がけましょうー

---
# リストから任意の要素を取り出す
> import random
> random.choice(list)

()の中に指定したリストから、任意の要素を出力する
```
>>> omikuji
['大吉', '中吉', '小吉', '吉', '凶']
>>> 
>>> import random
>>> random.choice(omikuji)
'凶'
>>> random.choice(omikuji)
'大吉'
```
---
# おみくじプログラムを改良しよう
+ random.choice(list)を使用してプログラムを改良する
	+ 変更前
	任意の整数を選択し、リストのオフセットを元におみくじ結果を選択
    + 変更後
	random.choice()を使用し、任意の要素を選択
---
# random.choice(list)を使用する
1. ファイル「04-1_list.py」をコピーし、ファイル名を「04-2_list.py」にする
2. ファイル名「04-2_list.py」を開く
3. 下記の部分を削除
```
# 乱数を生成
num = random.randrange(0,5)
```
---
# random.choice(list)を使用する
4. 変数「unsei」の中身を書き換える
+ 修正前
```
# omikuji[num]をunseiに代入
unsei = omikuji[num]
```
+ 修正後
```
#ランダムでおみくじを表示
unsei = random.choice(omikuji)
```
---
# 完成コード(1/2)
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
		   '中吉 まあまあよし',
		   '小吉 よし',
		   '吉 すこしよし',
		   '凶 わるし',
		   ]
```
---
# 完成コード(2/2)
```
#ランダムでおみくじを表示
unsei = random.choice(omikuji)

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```
---
# まとめ
+ リストとは
	+ 複数を要素をまとめた大きな箱
	+ 各要素には0からの番号が振られ、こちらを用いて値を取り出すことが可能
	+ リストの機能
	https://docs.python.jp/3/tutorial/datastructures.html#more-on-lists
---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ ~~おみくじの種類を増やそう~~
+ ~~名前を入力しよう~~
+ ~~自動で結果を出力しよう~~
+ ~~もっと短くしてみよう~~
+ 違う方法でやってみよう
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---
# 違う方法でやってみよう
+ 辞書を使っておみくじプログラムを改良してみよう！
---
# 辞書とは？
+ 定義方法
> 辞書名 = {鍵 : 値, 鍵 : 値, 鍵 : 値, ...}

+ 鍵と値で定義する
+ 「:」より左側が鍵の名前で、右側が鍵名に対応する値を示している
+ 定義した順番に表示されない
+ 鍵は重複不可

```
omikuji = {'daikichi': '大吉',
           'chukihi': '中吉',
           'shokichi': '小吉',
           'kichi': '吉',
           'kyo': '凶'}
```

+ リストのようにoffsetではなく、鍵名を使用して値を取り出す
```
>>> omikuji['daikichi']
'大吉'
```
---
# 対話モードで動作確認をしてみよう！
+ 辞書の定義
+ 鍵を使用しての値の取り出し
+ 追加
+ 削除
+ 値の変更(できないことを確認)
+ 鍵だけの取り出し
+ 値だけ取り出し
+ 鍵と値を取り出し

---
# 値の書き換え可否について
+ 値の書き換え可能(mutable)
	+ 箱の中身を出し入れ可能
	+ リスト
+ 値の書き換え不可能(immutable)
	+ 箱の蓋に鍵がかかっている
	+ 辞書、文字列
---
# おみくじプログラムの改良
+ リストを辞書に書き換える
+ random.choice(list)の()の中身を辞書から取り出した鍵にする
---
# リストを辞書に書き換える
1. ファイル「04-2_list.py」をコピーし、ファイル名を「05_dict.py」にする
2. ファイル名「05_dict.py」を開く
---
# リストを辞書に書き換える
3. リストの部分を辞書に書き換える
+ 修正前
```
# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
		   '中吉 まあまあよし',
		   '小吉 よし',
		   '吉 すこしよし',
		   '凶 わるし',
		   ]
```
+ 修正後
```
omikuji = {'daikichi': '大吉 すべてよし',
           'chukihi': '中吉 まあまあよし',
           'shokichi': '小吉 よし',
           'kichi': '吉 少しよし',
           'kyo': '凶 わるし'
}
```
---
# リストを辞書に書き換える
4. 変数「unsei」の中身を書き換える
+ 変更前
```
#ランダムでおみくじを表示
unsei = random.choice(omikuji)
```
+ 変更後
```
#辞書(omikuji)のkeyをランダム取得し、unsei_keyに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei_key = random.choice(list(omikuji.keys()))
```
---
# リストを辞書に書き換える
> list()

+ リストに変換する
```
>>> omikuji.keys()
dict_keys(['daikichi', 'cyukichi', 'syoukichi', 'kichi',
			'kyo'])
>>> 
>>> list(omikuji.keys())
['daikichi', 'cyukichi', 'syoukichi', 'kichi', 'kyo']
```
---
# 完成コード(1/2)
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# リスト(omikuji)を作成
omikuji = ['大吉 すべてよし',
		   '中吉 まあまあよし',
		   '小吉 よし',
		   '吉 すこしよし',
		   '凶 わるし',
		   ]
```

---
# 完成コード(2/2)
```
#ランダムでおみくじを表示
unsei = random.choice(omikuji)

print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei + 'です!')
```
---
# まとめ
+ 辞書とは
	　+ {鍵 : 値}の形で定義し、鍵を使用して値を取り出す
	　+ 順不同
	　+ 書き換え不可(immutable)
---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ ~~おみくじの種類を増やそう~~
+ ~~名前を入力しよう~~
+ ~~自動で結果を出力しよう~~
+ ~~もっと短くしてみよう~~
+ ~~違う方法でやってみよう~~
+ おみくじに仕事運を追加しよう
+ 「結果」によってメッセージを出力しよう

---
# おみくじに仕事運を追加しよう
+ 今までは「大吉」や「中吉」といった全体運だけ
+ このおみくじに「仕事運」の項目を追加する

+ リストの値を辞書にする
リストの中に辞書を入れる、辞書の値をリストにすることも可能
> 変数名 = [ {鍵:値}, {鍵:値}, {鍵:値},...]
```
omikuji = [
 {'all':全体運の内容1,'work':仕事運の内容1},
 {'all':全体運の内容2,'work':仕事運の内容2},...]
```
---
# 対話モードで動作確認をしてみよう！
+ 定義
+ 参照
+ 削除
+ 追加
---
# おみくじプログラムの改良
+ 変数「omikuji」の値に「仕事運」の項目を追加する

---
# 変数「omikuji」の値に「仕事運」の項目を追加する
1. ファイル「05_dict.py」をコピーし、ファイル名を「06_nest.py」にする
2. ファイル名「06_nest.py」を開く

---
# 変数「omikuji」の値に「仕事運」の項目を追加する
3.　変数「omikuji」を下記のように修正する
+ 修正前
```
omikuji = {'daikichi': '大吉 すべてよし',
           'chukihi': '中吉 まあまあよし',
           'shokichi': '小吉 よし',
           'kichi': '吉 少しよし',
           'kyo': '凶 わるし'}
```
+ 修正後
<font style = "font-size: 80%">
```
# 辞書が内包されたリストを作成
omikuji = [
 {'all':'大吉! すべてよし。 ','work':'仕事運:プロジェクトは大成功！'},
 {'all':'中吉! まぁまぁよし。 ','work':'仕事運:定時で帰れます！'},
 {'all':'小吉! よし。 ','work':'仕事運:ミスなく過ごせます！'},
 {'all':'吉! 少しよし。 ','work':'仕事運:思ったよりも上手くいくかも'},
 {'all':'凶! わるし。 ','work':'仕事運:些細なミスが命取りに！'}]
```
</font>

---
# 変数「omikuji」の値に「仕事運」の項目を追加する

4. random.choice()の修正
+ 修正前
```
#辞書(omikuji)のkeyをランダム取得し、unsei_keyに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei_key = random.choice(list(omikuji.keys()))
```
+ 修正後
```
#辞書(omikuji)のkeyをランダム取得し、unsei_keyに代入
# random.choiceするには、list化が必須のため、list()をしてます。
unsei_key = random.choice(list(omikuji.keys()))
```
---
# 変数「omikuji」の値に「仕事運」の項目を追加する
5. 出力結果の修正
<font style = "font-size: 80%">
+ 修正前
```
# 結果を出力
print(name + 'さんの運勢は、' + omikuji[unsei_key] +'です!')
```
+ 修正後
```
# 結果を出力
print(name + 'さんの運勢は、' + unsei['all']+ '\n' + unsei['work'])
```
</font>

---
# 完成コード(1/2)
<font style = "font-size: 80%">
  
```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 辞書が内包されたリストを作成
omikuji = [
 {'all':'大吉! すべてよし。 ','work':'仕事運:プロジェクトは大成功！'},
 {'all':'中吉! まぁまぁよし。 ','work':'仕事運:定時で帰れます！'},
 {'all':'小吉! よし。 ','work':'仕事運:ミスなく過ごせます！'},
 {'all':'吉! 少しよし。 ','work':'仕事運:思ったよりも上手くいくかも'},
 {'all':'凶! わるし。 ','work':'仕事運:些細なミスが命取りに！'}]

# omikuji内の辞書からランダムで取得
unsei = random.choice(omikuji)
```
</font>

---

# 完成コード(1/2)
<font style = "font-size : 80%">
  
```
print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei['all']+ '\n' + unsei['work'])
```
</font>

---

# まとめ
+ リストの要素を辞書にしたり、辞書の要素をリストにすることが可能

---

# 今日の内容

+ ~~プログラミングって？~~
+ ~~実際のプログラムを書いてみよう！~~
+ ~~おみくじの種類を増やそう~~
+ ~~名前を入力しよう~~
+ ~~自動で結果を出力しよう~~
+ ~~もっと短くしてみよう~~
+ ~~違う方法でやってみよう~~
+ ~~おみくじに仕事運を追加しよう~~
+ 「結果」によってメッセージを出力しよう

---

# おみくじ結果によってメッセージを出力する
+ 全体運に「吉」が含まれていた場合は「いい一日になるといいですね！」と出力する
+ 全体運が含まれていない場合は、「こういう日もあります。元気出してください！！」と出力する

---

# おみくじ結果によってメッセージを出力する
+ ifを使用して処理内容を変える
	+ 全体運に「吉」が含まれていた場合は(条件)「いい一日になるといいですね！」と出力する(処理)
+ 「含まれていた場合」には「in」を使用する
	+ '吉' in '大吉'
		+ 一致する(true)
	+ '吉' in '凶'
	    + 一致しない(false)
---
# おみくじプログラムを改良する
1. ファイル「06_nest.py」をコピーし、ファイル名を「07_if_in.py」にする
2. ファイル名「07_if_in.py」を開く
3. 一番下の行に下記を追加する
```
# 運勢が吉以上かで判断
if '吉' in unsei['all']:
	print('いい一日になるといいですね！')
else:
	print('こういう日もあります。元気出してくだい！！')
```

---

# 完成プログラム(1/2)
<font style = "font-size: 80%">

```
#!/usr/bin/env python3
# coding: utf-8

# モジュールをインポート
import random

# 辞書が内包されたリストを作成
omikuji = [
 {'all':'大吉! すべてよし。 ','work':'仕事運:プロジェクトは大成功！'},
 {'all':'中吉! まぁまぁよし。 ','work':'仕事運:定時で帰れます！'},
 {'all':'小吉! よし。 ','work':'仕事運:ミスなく過ごせます！'},
 {'all':'吉! 少しよし。 ','work':'仕事運:思ったよりも上手くいくかも'},
 {'all':'凶! わるし。 ','work':'仕事運:些細なミスが命取りに！'}]

# omikuji内の辞書からランダムで取得
unsei = random.choice(omikuji)
```

</font>

---

# 完成プログラム(1/2)
<font style = "font-size: 80%">
  
```
print('あなたの名前を入力してください')

# 名前を入力
name = input('>>')

# 結果を出力
print(name + 'さんの運勢は、' + unsei['all']+ '\n' + unsei['work'])

# 運勢が吉以上かで判断
if '吉' in unsei['all']:
	print('いい一日になるといいですね！')
else:
	print('こういう日もあります。元気出してください！！')
```

</font>

---
# まとめ
+ 「in」は「〜を含んでいる」という比較演算子

---

# 今日の内容振り返り

+ プログラミングって？(**指示内容を記述**)
+ 実際のプログラムを書いてみよう！(**print()**)
+ おみくじの種類を増やそう(**変数**)
+ 名前を入力しよう(**input()による入力**)
+ 自動で結果を出力しよう(**ifによる条件分岐**)
+ もっと短くしてみよう(**リスト**)
+ 違う方法でやってみよう(**辞書**)
+ おみくじに仕事運を追加しよう(**リストと辞書の組み合わせ**)
+ 「結果」によってメッセージを出力しよう(**in**)

みなさん長い間お疲れ様でした！

---
# 最後に
+ 次回予告
おみくじ内容をファイルから読み込んだり、書き込んだりする！

---
# アンケート
+ アンケートにご協力ください
+ tocaroグループ
疑問、不明点を気軽に聞いてください！
