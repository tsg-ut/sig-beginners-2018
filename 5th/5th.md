# TSG2018年Sセメスター初心者分科会\#5

今回はクラス。一応Pythonについては最終回にしようかなと思っています。

### Classとは
Classはいくつかの変数やメソッド（関数）をまとめて1つのグループとして扱えるものです（僕のイメージ）。Python含むオブジェクト指向系と強く結びつきがあると思います（個人の見解）。

例えば、ゲームを作る際に各プレイヤーの行う動作は1グループにまとまっていると都合が良いです。特に数多くのプレイヤーを動かす際（例えばボンバーマンなど）では各ターンごとに各プレイヤーの動作を行う関数を呼びます。

取り敢えず長文書くのもあれなので、コード例を出していこうと思います。
```python
class Human:
    name = ""
    def setName(self, name):
        self.name = name
    def Greet(self):
        print("%s says \"Hello!\""%self.name)

fiord = Human()
fiord.setName("fiord")
fiord.Greet() # ここで挨拶してくれる
```
これは何となく分かるかなと思います。`self`というのはクラスそのものを指し、今回の例では`self.name = fiord.name`と解釈してもらって問題ないと思います。この時、`self.name`を「属性（アトリビュート）」、`self.function(今回の例ではsetNameやGreet)`を「メソッド」といいます。ただ、そんな用語はどうでもいいのです。

因みに、`name = ""`で初期化をしていますが、無くてもsetNameをちゃんと最初に持ってくればGreetはちゃんと動作します。今回の例では`fiord`というグループの中に値をちゃんと入れているので。ここで、過去にやった似たやつと整理をします。
```python
a=3
def f():
    a = a + 2
f()
print(a) # 答えは何ですか？
```

これの答えは3です。ここで重要なのは、「関数外の変数は内部へ持ち込めるけど、値をコピーした別のものを使う」という点です。

つまり、関数内で`a = a + 2`をする際に`a`を外側から引っ張っています。そのため、その後`a = 5`となります。ただ、この`a(=5)`は関数内でしか使えない（スコープの問題）ので、関数の外でaを見ても何も変わっていません。

結果を反映させたいときには`global`を使うと外側のものそのものを持ってきてくれるんでした。

さて、肝心のクラスの方ですが、これは「メソッド内にて`self`でアクセスする際は`global`扱い」されます。つまり、そのクラスのメソッドの中ではそのクラスの属性にはアクセスが可能です。ただ、使いたいときは関数の引数に`self`を入れましょう。

__問題__ 何かメソッドを持つクラスを作ってください。

### コンストラクタとデストラクタ
コンストラクタとは「クラスオブジェクトが生成されるときに呼ばれる関数」、デストラクタは「クラスオブジェクトが削除されるときに呼ばれる関数」です。

以下のコードを見てみます。
```python
class Human:
    def __init__(self, name=""):
        self.name = name
        print("your name is %s!"%self.name)
    
    def __del__(self):
        print("boodbye %s!"%self.name)
    
    def Greet(self):
        print("%s says \"Hello!\""%self.name)

fiord = Human("fiord")  #__init__が呼ばれる
fiord.Greet()
del fiord   #__del__が呼ばれる
```
`del`はオブジェクトを削除するコマンドです。配列などでも使えます。
```python
>>> a=[1,2,3,4,5]
>>> del a[3]
>>> a
[1, 2, 3, 5]
```

コンストラクタは必ず呼ばれます。しかし、必ずしも定義する必要はありません（元々定義してあり、それを書き直す感じです）。一方、デストラクタは必ずしも呼ばれる保証がありません。そのため、基本的に定義することはありません。

__問題__ さっき作ったクラスにコンストラクタとデストラクタを定義してください。

### 継承
ゲームで自キャラの他にCPUが欲しいです。この時に`Character`というクラスの他に、「CPU独自の関数」というのも欲しくなります。こんな時に、`CPU`というクラスを定義したいです。しかし、殆ど同じ中身が同じものをコピペするのはものすごく効率が悪いです。（見づらくなりますし）

ということで、`CPU`というクラスを作るのですが、`Character`クラスの中身を全部持ってきたいときに使うのが継承です。

```python
class Human:
    def __init__(self, name=""):
        self.name = name
        print("your name is %s!"%self.name)
    
    def Greet(self):
        print("%s says \"Hello!\""%self.name)

class fiord(Human):
    def __init__(self, name=""):
        super().__init__(name)
        print("this class is fiord")
    
    def hoge(self):
        print("hogehoge%s"%self.name)

glacier = fiord("fiord") #2行printされます
print(glacier.name) #fiord
glacier.hoge()  #fiordが用いられる
glacier.Greet() #fiordが用いられる
```

という感じで、`Human`クラスの中身が`fiord`クラスに入ります。このときの`Human`は親クラス、`fiord`は子クラスです。`super().__init__()`と謎がありますが、これは親クラスのコンストラクタを呼んでいます。

当然といえば当然ですが、`fiord`クラスで定義した変数を`Human`のメソッドで用いることは出来ません。使いたいときはどうすればいいでしょうか？

### オーバーライド
継承による関数の書き換えです。さっき`__init__`がオーバーライドされていたんですが…
```python
class fiord(Human):
    def __init__(self, name=""):
        super().__init__(name)
        print("this class is fiord")
    
    def hoge(self):
        print("hogehoge%s"%self.name)
    
    def Greet(self):
        print("My name is fiord")

glacier = fiord("fiord")
glacier.Greet() # 再定義した方が使われる
```

というように上書きされます。因みに、他の言語では「オーバーロード」という概念があったりします。これは、引数の個数や型を変えることにより用いられる関数（同じ名前）を使い分けることです。Pythonにはありません。

実は多重継承という概念もあるのですが、変数の衝突などが複雑になります。この時間で説明がちょっと難しいので、[インターネットの記事](https://qiita.com/Tocyuki/items/155ec12bcd087803c817)を参考にしてみてください。

### privateとpublic
クラスは最後（とても速い）。今までのクラスでは普通に`glacier.name`でアクセスが出来ます。

ここでWebサービスを考えましょう。ログインが必要なタイプで、各ユーザーをクラスにまとめています。こんな時にユーザーの情報が外側でアクセスできるのが割と不味いらしいです（自分は理解していません）

ということで、外部からアクセスを許すか否かちゃんと決める必要があります。Pythonでは外部からアクセスを許さない場合のみ、加工を施します。

```python
class fiord(Human):
    def __init__(self, name=""):
        super().__init__(name)
        print("this class is fiord")
    
    def __hoge(self):
        print("hogehoge%s"%self.name)
    
    def Greet(self):
        print("My name is fiord")

glacier = fiord("fiord")
glacier.__hoge() # エラーが出る
```