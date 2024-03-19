import chess
import markdown
import status


def move_save_render(board: chess.Board, move: str) -> None:
    """This function receives a board and render it in a markdown file.
    :param board: An instantiated board.
    :type board: chess.Board
    :param move: A movement to be executed on any piece for both sides, black/white.
    :type move: str
    :return: None
    """
    try:
        board.parse_san(move)
    except chess.InvalidMoveError:
        raise ValueError(f"Invalid move {move}")
    except chess.IllegalMoveError:
        raise ValueError(f"Illegal move {move}")
    except chess.AmbiguousMoveError:
        raise ValueError(f"Ambiguous move {move}")
    else:
        move_confirmation = board.push_san(move)
        print(move_confirmation)
        status.save_game(board.fen())
        markdown.render_md(board)
