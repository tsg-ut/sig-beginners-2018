# TSG2018年Sセメスター初心者分科会\#7
一応最終回。ブロック崩しを実装してみましょう。ところで、ここに書くこととは…？

### [Pygame](https://www.pygame.org)とは
pythonでゲームを作れるライブラリ。使いやすいかというと微妙ですが

`pip install pygame`でインストールできます。

### ゲームの書き方について
##### importと初期化
```python
# モジュールのインポート
import pygame
from pygame.locals import *
# 初期化（必須）
pygame.init()
```
##### clock
アニメーションでは、高速で画像を切り替えることで「動いているように見える」というものです。ということで、ゲームでは基本的に
```python
while True:
    # 各フレームの処理
```
となるのですが、例えば3msで処理が終わるフレームもあれば、29msで終わる処理もあるでしょう。ただ`while True`とするだけでは各フレーム毎の差で見づらくなってしまいます。そのため、毎回同じ更新頻度になるように時間調整（ただ待つだけ）を行うのがclockです。60fpsにするときは
```python
clock = pygame.time.Clock()
while True:
    clock.tick(60)
```
たったこれだけです。