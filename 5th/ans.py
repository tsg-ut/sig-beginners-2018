import random
import re #正規表現用

num = [random.randint(0, 9) for _ in range(4)] # 4つのカードを生成
# tips: for _ in range(4)での_はfor文の中では使えませんが、被らないので2重ループが出来ます。
# 例 [["a" for _ in range(3)] for _ in range(4)]は"a"が12個生成されます

# ユニークにするなら
for i in range(1,4):
    while num[i] in num[:i]:
        num[i] = random.randint(0,9)

cnt = 0

# 余計なことを考えない入力
def easyInput():
    return list(map(int,input("数字を4つ入力してください").split()))
# 色々考える入力
# 正規表現というワードがあり、文字列がちゃんとしているか調べられます。
def hardInput():
    s = input("数字を4つ入力してください")
    if re.match("^(\d ){3}\d$",s):
        return list(map(int,s.split()))
    else:
        return "error"

while True:
    cnt+=1
    a = hardInput()
    if isinstance(a,str):
        continue
    # 取り敢えずブロウを出す
    blow = 0
    for i in range(4):
        if a[i] in num:
            blow+=1
    # 次にヒット
    hit = 0
    for i in range(4):
        if a[i]==num[i]:
            hit+=1
            blow-=1
    print("{0}ヒット{1}ブロウ".format(hit, blow))
    if hit==4:
        print("かかったターン数:{0}".format(cnt))
        break