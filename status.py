import utils


def save_game(fen: str) -> None:
    """This function receives a game status and saves in a file.
    :param fen: A Forsythe-Edwards Notation (FEN) formatted string.
    :type fen: str
    :return: None
    """
    if utils.validate_fen(fen):
        f = open("chess", "w")
        f.write(fen)
        f.close()


def load_game() -> str:
    """This function loads a game status from a file. If there is no previous game status, returns a not initiated one.
    :return: A Forsythe-Edwards Notation (FEN) formatted string. E.g.: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    :rtype: str
    """
    try:
        f = open("chess", "r")
        fen = f.read()
    except FileNotFoundError:
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    else:
        f.close()
    return fen
