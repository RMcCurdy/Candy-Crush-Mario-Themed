def is_adjacent(a, clickOneRow, clickOneColumn, clickTwoRow, clickTwoColumn):
    true_or_false = False
    # adjacent down?
    if clickOneRow == clickTwoRow + 1 and clickOneColumn == clickTwoColumn:
        true_or_false = True
    # adjacent up?
    if clickOneRow == clickTwoRow - 1 and clickOneColumn == clickTwoColumn:
        true_or_false = True
    # adjacent right?
    if clickOneRow == clickTwoRow and clickOneColumn == clickTwoColumn + 1:
        true_or_false = True
    # adjacent left?
    if clickOneRow == clickTwoRow and clickOneColumn == clickTwoColumn - 1:
        true_or_false = True

    return true_or_false


def swap(firstClickCell, secondClickCell):
    return secondClickCell, firstClickCell


def swap_cells(a, clickOneRow, clickOneColumn, clickTwoRow, clickTwoColumn):
    swapTuple = swap(a[clickOneRow][clickOneColumn], a[clickTwoRow][clickTwoColumn])
    a[clickOneRow][clickOneColumn] = swapTuple[0]
    a[clickTwoRow][clickTwoColumn] = swapTuple[1]
    return a

