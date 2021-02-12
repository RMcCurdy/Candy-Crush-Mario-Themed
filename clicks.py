import stddraw
from board import draw_game_board

def click(a):
    click_row = False
    click_row = False
    first_click = False
    while first_click is False:
        stddraw.show(0.0)
        if stddraw.mousePressed():
            mx = stddraw.mouseX()
            my = stddraw.mouseY()
            if 5 < mx < 488 and 5 < my < 635:
                for i in range(9):
                    for j in range(7):
                        if (5 + 70 * j) < mx < (5 + 70 * (j + 1)) and (635 - 70 * i) > my > (635 - 70 * (i + 1)):
                            click_row = i
                            click_column = j

                break

    return click_row, click_column


def highlight_click(a, row, column):
    a[row][column] = a[row][column] + 6
    draw_game_board(a)
    a[row][column] = a[row][column] - 6
