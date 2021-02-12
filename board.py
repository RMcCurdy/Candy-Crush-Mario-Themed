import images
import stddraw
import color
import random

def set_parameters():
    stddraw.setXscale(0,500)
    stddraw.setYscale(0,800)
    stddraw.setCanvasSize(500,800)


def main_menu():
    stddraw.picture(images.background, 250, 400)
    stddraw.picture(images.welcome, 250, 680)
    stddraw.picture(images.button, 250, 420)
    stddraw.picture(images.mario, 130, 150)
    stddraw.picture(images.luigi, 370, 150)
    stddraw.show(0.0)


def draw_game_board(array):
    # global score
    for i in range(9):
        diff = 35
        for j in range(7):
            if array[i][j] == 0:
                stddraw.picture(images.icon0, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 1:
                stddraw.picture(images.icon1, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 2:
                stddraw.picture(images.icon2, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 3:
                stddraw.picture(images.icon3, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 4:
                stddraw.picture(images.icon4, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 5:
                stddraw.picture(images.icon5, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 6:
                stddraw.picture(images.icon0Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 7:
                stddraw.picture(images.icon1Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 8:
                stddraw.picture(images.icon2Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 9:
                stddraw.picture(images.icon3Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 10:
                stddraw.picture(images.icon4Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 11:
                stddraw.picture(images.icon5Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 13:
               stddraw.picture(images.icon6, 5 + j*70 + diff, 635 - i*70 - diff)
               # score += 1
               # stddraw.picture(scoreOverlay,327,725)
               # stddraw.setFontSize(25)
               # stddraw.setPenColor(color.WHITE)
               # stddraw.text(327, 725, str(score))
    stddraw.show(0.0)

def draw_game_board_yeet(array):
    # global score
    for i in range(9):
        diff = 35
        for j in range(7):
            if array[i][j] == 0:
                stddraw.picture(images.icon0, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 1:
                stddraw.picture(images.icon1, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 2:
                stddraw.picture(images.icon2, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 3:
                stddraw.picture(images.icon3, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 4:
                stddraw.picture(images.icon4, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 5:
                stddraw.picture(images.icon5, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 6:
                stddraw.picture(images.icon0Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 7:
                stddraw.picture(images.icon1Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 8:
                stddraw.picture(images.icon2Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 9:
                stddraw.picture(images.icon3Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 10:
                stddraw.picture(images.icon4Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 11:
                stddraw.picture(images.icon5Click, 5 + j*70 + diff, 635 - i*70 - diff)
            if array[i][j] == 13:
               stddraw.picture(images.icon6, 5 + j*70 + diff, 635 - i*70 - diff)
               # score += 1
               # stddraw.picture(scoreOverlay,327,725)
               # stddraw.setFontSize(25)
               # stddraw.setPenColor(color.WHITE)
               # stddraw.text(327, 725, str(score))
    stddraw.show(150.0)

Clicked = False


def main_menu_click():
    global Clicked
    while not Clicked:
        if stddraw.mousePressed():
            mx = stddraw.mouseX()
            my = stddraw.mouseY()
            # determines where and what to print
            if 446 > mx > 54 and 539 > my > 301:
                stddraw.picture(images.gameBackground,250,400)
                stddraw.picture(images.scoreOverlay,327,725)
                stddraw.setFontSize(25)
                stddraw.setPenColor(color.WHITE)
                stddraw.text(327,725, '0')
                Clicked = True
        stddraw.show(0.0)


def generate_board():
    a = []
    for i in range(9):
        a.append([])
        for j in range(7):
            if i < 2 and j < 2:
                a[i].append(random.randrange(0, 6))
            if i < 2 and 2 <= j <= 6:
                a[i].append(random.randrange(0, 6))
                while a[i][j] == a[i][j-2] and a[i][j] == a[i][j-1]:
                    a[i][j] = random.randrange(0, 6)
            if 2 <= i <= 8 and j < 2:
                a[i].append(random.randrange(0, 6))
                while a[i][j] == a[i-2][j] and a[i][j] == a[i-1][j]:
                    a[i][j] = random.randrange(0, 6)
            if 2 <= i <= 8 and 2 <= j <= 6:
                a[i].append(random.randrange(0, 6))
                while (a[i][j] == a[i][j - 2] and a[i][j] == a[i][j - 1]) or (a[i][j] == a[i-2][j] and a[i][j] == a[i-1][j]):
                    a[i][j] = random.randrange(0, 6)
                    while (a[i][j] == a[i][j - 2] and a[i][j] == a[i][j - 1]) and (a[i][j] == a[i - 2][j] and a[i][j] == a[i - 1][j]):
                        a[i][j] = random.randrange(0, 6)
    return a