import re

import chess

r = r"^([kqrbnpKQRBNP12345678]{1,8}\/){7}[kqrbnpKQRBNP12345678]{1,8}\s[wb]\s(((([kqKQ])(?!\5)){1,4})|-)\s(([a-h][1-8])|-)\s\d+\s[1-9]\d*$"
color_turn = r"(\s[wb]\s)"


def which_color_plays_fen(fen: str) -> str:
    """This function receives a game status and return which color plays in the current turn.
    :param fen: A Forsythe-Edwards Notation (FEN) formatted string.
    :type fen: str
    :return: A string indicating the right color. 'WHITE' | 'BLACK'
    :rtype: str
    """
    x = re.search(color_turn, fen).group()
    if x == ' w ':
        return 'WHITE'
    else:
        return 'BLACK'


def which_color_plays_board(board: chess.Board) -> bool:
    """This function receives a game status and return which color plays in the current turn.
    :param board: An instantiated board.
    :type board: chess.Board
    :return: A bool indicating the right color. 'WHITE' | 'BLACK'
    :rtype: bool
    """
    return board.turn


def validate_fen(fen: str) -> bool:
    """This function receives a game status and validate the format.
    :param fen: A Forsythe-Edwards Notation (FEN) formatted string.
    :type fen: str
    :return: Whether the FEN is valid or not. True | False
    :rtype: bool
    """
    x = re.search(r, fen).group()
    if x is not None:
        return True
    else:
        return False
