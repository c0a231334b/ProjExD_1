import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")  # ウィンドウのタイトル（p.53）Surfaceを作成
    screen = pg.display.set_mode((800, 600))      # ウィンドウのサイズ（p.49）
    clock  = pg.time.Clock()                      # クロックの生成（p.58）
    bg_img = pg.image.load("fig/pg_bg.jpg")           # 背景画像surfaceを作成（p.61）
    kk_img = pg.image.load("fig/3.png")               # こうかとんsurfaceを作成（p.61）
    kk_img = pg.transform.flip(kk_img, True, False)      # 画像を反転（p.61）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])           # screen Surfaceに背景描画surfaceを貼り付ける（p.53）
        screen.blit(kk_img, [300, 200])       # screen Surfaceにこうかとんsurfaceを貼り付ける（p.53）
        pg.display.update()
        tmr += 1        
        clock.tick(200)  #FPSを200に設定（p.58）


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()