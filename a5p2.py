import stddraw
import color
import images
from picture import Picture

import board
from board import generate_board
from board import draw_game_board
from board import draw_game_board_yeet

from clicks import click
from clicks import highlight_click

from swap import is_adjacent
from swap import swap_cells

from delete import delete_combination
from delete import is_combination

from fall import cleared_cells
from fall import is_fall
from fall import cells_fall
from fall import generate_tile

# sets parameters for canvas
board.set_parameters()

# creates main menu
board.main_menu()

# if main menu button is clicked, game begins
board.main_menu_click()

# generates a randomized board.
a = generate_board()

# draws initial game board.
draw_game_board(a)

# if score >= 100, the game will end.
score = 0

# if game_on is False, the game will end.
game_on = True

# runs the game
while game_on is True:
    """
    Program waits for first click
    """
    # assigns clickOne as a tuple of the values of clickOneColumn and clickOneRow (a[i], a[i][j])
    clickOne = click(a)
    # redraws game board, but with clickOne's tile highlighted
    highlight_click(a, clickOne[0], clickOne[1])

    """
    Program waits for second click
    """
    # assigns clickTwo as a tuple of the values of clickTwoColumn and clickTwoRow (a[i], a[i][j])
    clickTwo = click(a)

    """
    Program deletes cells if clicked cells are adjacent and make a combination
    """
    # checks if the selected tiles are adjacent
    if is_adjacent(a, clickOne[0], clickOne[1], clickTwo[0], clickTwo[1]) is True:
        a = swap_cells(a, clickOne[0], clickOne[1], clickTwo[0], clickTwo[1])
        draw_game_board_yeet(a)
        # checks if moving the tiles would create a combination

        if is_combination(a, clickOne[0], clickOne[1]) is True or is_combination(a, clickTwo[0], clickTwo[1]) is True:
            a = delete_combination(a, clickOne[0], clickOne[1])
            a = delete_combination(a, clickTwo[0], clickTwo[1])
            draw_game_board_yeet(a)

        else:
            a = swap_cells(a, clickOne[0], clickOne[1], clickTwo[0], clickTwo[1])
            draw_game_board_yeet(a)

    else:
        draw_game_board_yeet(a)

    """
    Program moves cells down to fill in open spaces, 
    if combination is present after falling into place, delete combination
    generate tile, 
    repeat until no open spaces
    """


    while cleared_cells(a) is True:
        while is_fall(a) is True:

            # returns game board, columnOfFallenTile, rowOfFallenTile

            fall_tuple = cells_fall(a)
            draw_game_board(a)


            # checks if a combination exists at the cell the tile fell to and deletes if True
            # if fall_tuple[1] is not None and fall_tuple[2] is not None:
            if is_combination(a, fall_tuple[1], fall_tuple[2]) is True:
                delete_combination(a, fall_tuple[1], fall_tuple[2])
                draw_game_board(a)

        generateTuple = generate_tile(a)
        score += generateTuple[3]
        stddraw.setFontSize(25)
        stddraw.setPenColor(color.WHITE)
        stddraw.picture(images.scoreOverlay, 327, 725)
        stddraw.text(327, 725, str(score))
        draw_game_board(a)
        if generateTuple[1] is not None and generateTuple[2] is not None:
            if is_combination(a, generateTuple[1], generateTuple[2]) is True:
                delete_combination(a, generateTuple[1], generateTuple[2])
                draw_game_board(a)

    """
    Program checks if score exceeds winning condition
    """
    if score >= 100:
        game_on = False
        stddraw.picture(images.youWinBackground, 250, 400)
        stddraw.show()