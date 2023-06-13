import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230613/fig/pg_bg.jpg")
    koukaton_img = pg.image.load("ex01-20230613/fig/3.png")
    koukatonReverse_img = pg.transform.flip(koukaton_img, True, False)
    koukatonReverseRotate10_img = pg.transform.rotate(koukatonReverse_img, 10)
    tmr = 0

    rensyu3 = list[koukatonReverse_img, koukatonReverseRotate10_img]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(koukatonReverse_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(10)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()