import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")      # ウィンドウのタイトル（p.53）Surfaceを作成
    screen = pg.display.set_mode((800, 600))          # ウィンドウのサイズ（p.49）
    clock  = pg.time.Clock()                          # クロックの生成（p.58）
    bg_img = pg.image.load("fig/pg_bg.jpg")           # 背景画像surfaceを作成（p.61）
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 背景画像surfaceを作成（p.61）
    kk_img = pg.image.load("fig/3.png")               # こうかとんsurfaceを作成（p.61）
    kk_img = pg.transform.flip(kk_img, True, False)   # 画像を反転（p.61）
    kk_rct = kk_img.get_rect()        
    kk_rct.center = 300, 200                # こうかとんrectを取得する（p.50）
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        kk_rct.move_ip(-1, 0)
        key_lst = pg.key.get_pressed()        # キー入力を取得（p.62）
        if key_lst[pg.K_UP]:                  # 上矢印キーが押されている場合
            kk_rct.move_ip(0, -1)             # 左上に移動
        if key_lst[pg.K_DOWN]:                # 上矢印キーが押されている場合
            kk_rct.move_ip(0, +1)             # 左下に移動
        if key_lst[pg.K_LEFT]:                # 左矢印キーが押されている場合
            kk_rct.move_ip(-1, 0)             # 左に移動
        if key_lst[pg.K_RIGHT]:               # 右矢印キーが押されている場合
            kk_rct.move_ip(+2, 0)             # 右に移動

        x = -(tmr % 3200) #練習6-2（p.67）
        screen.blit(bg_img,  [x, 0])           # screen Surfaceに背景描画surfaceを貼り付ける（p.53）tmrを入れると背景が左にスクロールする（p.61）
        screen.blit(bg_img2, [x + 1600, 0])
        screen.blit(bg_img,  [x + 3200, 0])
        screen.blit(bg_img2, [x + 4800, 0])

        screen.blit(kk_img, kk_rct)           # screen Surfaceにこうかとんsurfaceを貼り付ける（p.53）
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)  #FPSを200に設定（p.58）


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()