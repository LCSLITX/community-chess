import chess
import markdown
import status
import wrapper


def game(move: str) -> None:
    """Load fen, instantiate board, move a piece, saving the board (fen) and rendering markdown.
    :param move: A movement to be executed on any piece for both sides, black/white.
    :type move: str
    :return: None
    """
    # Instantiate
    fen = status.load_game()
    board = chess.Board(fen)

    # Move, save and render
    if move is not None:
        wrapper.move_save_render(board, move)
    else:
        # Save and render
        status.save_game(board.fen())
        markdown.render_md(board)
