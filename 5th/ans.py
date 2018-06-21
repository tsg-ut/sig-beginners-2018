import random

num = [random.randint(0, 9) for _ in range(4)] # 4つのカードを生成
# tips: for _ in range(4)での_はfor文の中では使えませんが、被らないので2重ループが出来ます。
# 例 [["a" for _ in range(3)] for _ in range(4)]は"a"が12個生成されます

# ユニークにするなら
for i in range(1,4):
    while num[i] in num[:i]:
        num[i] = random.randint(0,9)

cnt = 0

# 余計なことを考えない
def easyInput():
    return list(map(int,input("数字を4つ入力してください").split()))

while True:
    cnt+=1
    a = easyInput()

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