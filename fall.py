import random
def cleared_cells(a):
    true_or_false = False
    for i in range(9):
        for j in range(7):
            if a[i][j] == 13:
                true_or_false = True
    return true_or_false

def is_fall(a):
    true_or_false = False
    for i in range(8):
        for j in range(7):
            if a[i][j] != 13 and a[i+1][j] == 13:
                true_or_false = True

    return true_or_false


def cells_fall(a):
    rowOfTileThatFell = None
    columnOfTileThatFell = None
    for i in range(8):
        for j in range(7):

            if a[i][j] != 13 and a[i + 1][j] == 13:
                falling = True
                x = 0
                while falling is True:
                    if i + x + 1 < 9:
                        if a[i + x][j] != 13 and a[i + x + 1][j] == 13:
                            a[i + x + 1][j] = a[i + x][j]
                            a[i + x][j] = 13
                            rowOfTileThatFell = i + 1 + x
                            columnOfTileThatFell = j
                            x += 1
                        else:
                            falling = False
                    else:
                        falling = False
                return a, rowOfTileThatFell, columnOfTileThatFell

    return a, rowOfTileThatFell, columnOfTileThatFell


def generate_tile(a):
    score = 0
    row = None
    column = None
    for i in range(1):
        for j in range(7):
            if a[i][j] == 13:
                a[i][j] = random.randrange(0, 6)
                row = i
                column = j
                score = 1
                return a, row, column, score

    return a, row, column, score