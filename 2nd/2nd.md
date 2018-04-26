# TSG2018年Sセメスター初心者分科会\#2

### 前回忘れていた事項
「コメントアウト」…ソースコードの一部をコメントとして扱ってもらい、その部分は実行しないでもらう
```python
# 「#」以降はその行ではコメント扱いです。
"""
厳密に正しいのかといわれると微妙なんですが、
複数行コメントではこのようにダブルクォーテーション×3で囲います。
実際にはこれはコメント扱いではなく、改行を含む文字列という扱いになっています。
"""
```
上のコードはソースコード上では文字列を捨てるだけで何もしません。「インタラクティブモード」ならこれが文字列として評価されるので、それが出力されます。

***

### 型について
取り敢えず知っておきたいのは

- int   3,5,8<br>
上限・下限はありません。

- float 3.14,1.41,2.27<br>
double型は存在しないので、恐らく64bit浮動小数点型

- string "hoge","fuga","piyo"<br>
文字列。文字もstring。結構面倒で、「文字単位の変更は出来ない」という特徴があります。基本的な扱い方はlistと同じ

- list [1,3,4],["hoge","fuga","nya-n"],["hoge",3,[4.1,"nya-n"]]
配列です。中身の型が統一されている必要は無いです。

の4つ。いろんな型が存在するのですが、変数を宣言するときに型は宣言する必要は無く、インタプリタがうまい具合にやってくれます。

他にもsetとかdictとかありますが、それらは後で紹介します。

ここで、「キャスト」という概念を教えます。簡単に言うと型の変更です。以下のコードを実行してみてください。
```python
>>> int(3.14)
3
>>> float(3)
3.0
>>> float("5.12")
5.12
>>> int("3920")
3920
>>> str(32)
'32'
>>> str(2.236)
'2.236'
>>> list("hoge")
['h', 'o', 'g', 'e']
>>> str(["h","o","g","e"])
"['h', 'o', 'g', 'e']"
```
このように、int⇔float⇔stringは割と自由が利きます。また、string→listは出来ますが、その逆はダメですね…ではどうすれば文字の連結が出来るんでしょうか？

***

### list/stringの扱い

##### list
配列です。
```python
>>> a=[1,2,3,4,5]
>>> a[3]    #1つ目の要素を0番目として扱います
4
>>> print(a)
[1, 2, 3, 4, 5]
>>> a[5]    #6番目にアクセスしようとするとエラーが出ます
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> a[-1]   #負の数は右から何番目かでアクセスできます。
5
>>> a[-2]
4
>>> a[2]=4  #値は変更可
>>> a
[1, 2, 4, 4, 5]
>>> a[:3]   #独特だけど部分配列を作ります（スライスと言います）
[1, 2, 4]
>>> a[1:]
[2, 4, 4, 5]
>>> a[::2]  #奇数番目のみを取得(2ずつ進める)
[1, 4, 5]
```

このリストには多様な関数が用意されています。
```python
>>> max(a)
5
>>> sum(a)
16
>>> len(a)  #配列の長さ（配列の要素数）
5
>>> map(str,a)  #aの各要素をstrに変えます。
<map object at 0x05CE3C10>
>>> list(map(str,a))    #ただ、Python3ではmap objectというもので返されるのでlistにキャスト
['1', '2', '4', '4', '5']
```

__問題__ a=[2,3,5,4,42,625,2,7,52,435,46]の平均値を求めてください。

##### string
stringも配列と同様に扱えます。また、string専用の関数も結構あります。
```python
>>> s="TSG_sig-beginners-2018"
>>> s*3
'TSG_sig-beginners-2018/04/26TSG_sig-beginners-2018/04/26TSG_sig-beginners-2018/04/26'
>>> len(s)
22
>>> s[14]
'e'
>>> s[:8]
'TSG_sig-'
>>> s[3:19]
'_sig-beginners-2'
>>> s[12:-4]
'nners-'
>>> s.replace("sig","SIG")  #文字列の置換
'TSG_SIG-beginners-2018'
>>> s[:3].lower()   #小文字に変更。大文字に変更はupper。
'tsg'
>>> s[3]="-"    #ただ、文字の変更ができません。
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> slist=list(s)   #なので、一回リストにして
>>> slist
['T', 'S', 'G', '-', 's', 'i', 'g', '-', 'b', 'e', 'g', 'i', 'n', 'n', 'e', 'r', 's', '-', '2', '0', '1', '8']
>>> slist[3]="-"    #これは文字列全体を変更しているのでOKです。
>>> "".join(slist)  #「中身が全て文字列のリスト」→stringはこのようにします。各要素の間に空文字を突っ込んでいる感じ。
'TSG-sig-beginners-2018'
>>> s+="/04/26"     #ちょっと分かりづらいけど、s=s+"/04/26"で文字列全体を変更しているのでOK
>>> s
'TSG_sig-beginners-2018/04/26'
```

***

### if
場合分けに用います。
```python
x=7
if x>5:
    print("x is larger than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is smaller than 5")
```
ifの実行内容の範囲はインデントを行います。ifが成立しない時はelifを見て、それも成立しないならelseが実行されます。__コロンとインデントが大事です。__

##### boolean型について
上では触れませんでしたが、boolean型というものがあります。TrueとFalseの2種類のみが存在します。ifでその内部を行うかどうかはboolean型にキャストを行って判定します。

Trueならif文章の中身が実行されます。
```python
>>> 1>0
True
>>> 0==1
False
>>> "1"==1
False
>>> 3>=3
True
>>> True and False
False
>>> True and True
True
>>> False or True
True
>>> False or False
False
>>> True ^ True
False
>>> False ^ True
True
```

***