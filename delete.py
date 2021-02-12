def check_top(a, row, column):
    check_top_down_check = False
    check_mid_value = False

    # checks if cell is between same up and same down
    if row > 0:
        if a[row][column] == a[row + 1][column] and a[row][column] == a[row - 1][column]:
            check_top_down_check = True
            check_mid_value = True


    # checks if multiple of the same cell above
    i = 1
    if a[row][column] == a[row + 1][column] and a[row][column] == a[row + 2][column]:
        check_mid_value = True
        while a[row][column] == a[row + i][column] and 0 <= row + i < 8:
            a[row + i][column] = 13
            if a[row][column] == a[row+i+1][column] and row+i+1 == 8:
                a[row + i + 1][column] = 13
            i += 1

    return a, check_top_down_check, check_mid_value


def check_bottom(a, row, column):
    check_bot_top_check = False
    check_mid_value = False

    # checks if cell is between same down and same up
    if row < 8:
        if a[row][column] == a[row - 1][column] and a[row][column] == a[row + 1][column]:
            check_bot_top_check = True
            check_mid_value = True

    # checks if multiple of the same cell above
    i = 1
    if a[row][column] == a[row - 1][column] and a[row][column] == a[row - 2][column]:
        check_mid_value = True
        while a[row][column] == a[row - i][column] and 0 < row - i <= 8:
            a[row - i][column] = 13
            if a[row][column] == a[row - i - 1][column] and row - i - 1 == 0:
                a[row - i - 1][column] = 13
            i += 1

    return a, check_bot_top_check, check_mid_value


def check_right(a, row, column):
    check_right_left_check = False
    check_mid_value = False

    # checks if cell is between same right and same left
    if column > 0:
        if a[row][column] == a[row][column + 1] and a[row][column] == a[row][column - 1]:
            check_right_left_check = True
            check_mid_value = True

    # checks if multiple of the same cell above
    i = 1
    if a[row][column] == a[row][column + 1] and a[row][column] == a[row][column + 2]:
        check_mid_value = True
        while a[row][column] == a[row][column + i] and 0 <= column + i < 6:
            a[row][column + i] = 13
            if a[row][column] == a[row][column + i + 1] and column + i + 1 == 6:
                a[row][column + i + 1] = 13
            i += 1

    return a, check_right_left_check, check_mid_value


def check_left(a, row, column):
    check_left_right_check = False
    check_mid_value = False

    # checks if cell is between same right and same left
    if column < 6:
        if a[row][column] == a[row][column - 1] and a[row][column] == a[row][column + 1]:
            check_left_right_check = True
            check_mid_value = True

    # checks if multiple of the same cell above
    i = 1
    if a[row][column] == a[row][column - 1] and a[row][column] == a[row][column - 2]:
        check_mid_value = True
        while a[row][column] == a[row][column - i] and 0 < column - i <= 6:
            a[row][column - i] = 13
            if a[row][column] == a[row][column - i - 1] and column - i - 1 == 0:
                a[row][column - i - 1] = 13
            i += 1

    return a, check_left_right_check, check_mid_value


def delete_combination(a, row, column):

    topTuple = [False, False, False]
    bottomTuple = [False, False, False]
    rightTuple = [False, False, False]
    leftTuple = [False, False, False]

    if row < 7:
        topTuple = check_top(a, row, column)
        a = topTuple[0]
    if row > 1:
        bottomTuple = check_bottom(a, row, column)
        a = bottomTuple[0]
    if column < 5:
        rightTuple = check_right(a, row, column)
        a = rightTuple[0]
    if column > 1:
        leftTuple = check_left(a, row, column)
        a = leftTuple[0]

    if topTuple[1] is True:
        a[row - 1][column] = 13
        a[row + 1][column] = 13
    if bottomTuple[1] is True:
        a[row + 1][column] = 13
        a[row - 1][column] = 13
    if rightTuple[1] is True:
        a[row][column - 1] = 13
        a[row][column + 1] = 13
    if leftTuple[1] is True:
        a[row][column + 1] = 13
        a[row][column - 1] = 13

    if topTuple[2] is True or bottomTuple[2] is True or rightTuple[2] is True or leftTuple[2] is True:
        a[row][column] = 13
    return a


def check_top_gang(a, row, column):
    check_mid_value = False

    # checks if cell is between same up and same down
    if row > 0:
        if a[row][column] == a[row + 1][column] and a[row][column] == a[row - 1][column]:
            check_mid_value = True

    # checks if multiple of the same cell above
    if a[row][column] == a[row + 1][column] and a[row][column] == a[row + 2][column]:
        check_mid_value = True

    return check_mid_value


def check_bottom_gang(a, row, column):
    check_mid_value = False

    # checks if cell is between same down and same up
    if row < 8:
        if a[row][column] == a[row - 1][column] and a[row][column] == a[row + 1][column]:
            check_mid_value = True

    # checks if multiple of the same cell above
    if a[row][column] == a[row - 1][column] and a[row][column] == a[row - 2][column]:
        check_mid_value = True

    return check_mid_value


def check_right_gang(a, row, column):
    check_mid_value = False

    # checks if cell is between same right and same left
    if column > 0:
        if a[row][column] == a[row][column + 1] and a[row][column] == a[row][column - 1]:
            check_mid_value = True

    # checks if multiple of the same cell above
    if a[row][column] == a[row][column + 1] and a[row][column] == a[row][column + 2]:
        check_mid_value = True

    return check_mid_value


def check_left_gang(a, row, column):
    check_mid_value = False

    # checks if cell is between same right and same left
    if column < 6:
        if a[row][column] == a[row][column - 1] and a[row][column] == a[row][column + 1]:
            check_mid_value = True

    # checks if multiple of the same cell above
    if a[row][column] == a[row][column - 1] and a[row][column] == a[row][column - 2]:
        check_mid_value = True

    return check_mid_value


def is_combination(a, row, column):
    true_or_false = False

    top = False
    bottom = False
    right = False
    left = False

    if row < 7:
        top = check_top_gang(a, row, column)
    if row > 1:
        bottom = check_bottom_gang(a, row, column)
    if column < 5:
        right = check_right_gang(a, row, column)
    if column > 1:
        left = check_left_gang(a, row, column)

    if top is True or bottom is True or right is True or left is True:
        true_or_false = True

    return true_or_false
