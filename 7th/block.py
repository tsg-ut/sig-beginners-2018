import pygame
from pygame.locals import *
import sys
import random
import math

# 初期化。画面サイズは適当に決めて。
w = 1280
h = 720
SCREEN_SIZE = (w, h)
pygame.init()

# 画面の大きさの指定。引数の2番目をFULLSCREENにするとフルスクリーンになります
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Block")

# Phase 3:ブロックを設置しよう
# ブロックオブジェクト。

# Phase 2: バーを生やそう
# バー
class Bar:
    
# Phase 1:ボールを表示、動かそう
# ボールオブジェクト
class Ball:
    # pos=(x,y):ボールの中心の座標
    # v=(vx,vy):ボールの移動速度(1フレーム当たり)
    # a:壁で反発する際の加速度合
    # r:ボールの半径
    def __init__(self, pos = (0, 0), v = (0, 0), a = 1.0, r = 10):
        
    # 衝突しているか判定(直線なのでbarとblock共通)
    def conflict(self, obj):
        
    # 1フレーム分動かします
    # blocks: 現在残っているブロックのオブジェクトデータ
    def move(self, blocks = []):
        

# クロック（後で使います）
clock = pygame.time.Clock()
# メインループ
while True:
    # 30fpsに調整
    clock.tick(30)
    # 背景
    screen.fill((255, 255, 255))

    # バーを移動
    bar.move()
    # ボールを移動させる
    ball.move()
    # ブロックを削除する
    
    # ボール、ブロックの表示
    # pygame.draw.circle(screen, (R,G,B), (X,Y), R)

    # screen.fill((R,G,B), Rect(x,y,w,h))

    for i in range(len(blocks)):
        # pygame.draw.rect(screen, (R,G,B), Rect(x,y,w,h))


    # イベント処理
    for event in pygame.event.get():
        # キーボードが押された時
        if event.type == KEYDOWN:
            # ゲームの終了
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    # 画面を表示
    pygame.display.update()