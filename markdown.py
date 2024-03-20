import chess
import constants
import utils

# { from_square: [to_square...] }
# E.g.: { 'd1': ['f3', 'c3', 'e1', 'a1'], 'a4': ['c3', 'a2'] }
legal_moves: dict[str, list[str]] = {}


def render_md(board: chess.Board) -> None:
    """This function receives a board and render it in a markdown file.
    :param board: An instantiated board.
    :type board: chess.Board
    :return: None
    """
    text: str = f"{constants.title}{constants.board_columns}{constants.board_div}"

    for line, move in enumerate(board.legal_moves):
        # For some reason, `move` is already in UCI notation instead of SAN.
        move_str = str(move)
        from_square = move_str[:2]
        to_square = move_str[-3:] if len(move_str) == 5 else move_str[-2:]
        if from_square not in legal_moves.keys():
            legal_moves[from_square] = []
        legal_moves[from_square].append(to_square)

    md_board: list[list] = [["" for _ in range(8)] for _ in range(8)]  # creates 8x8 array

    ranks_list: list[str] = str(board).splitlines()

    for line, rank in enumerate(ranks_list):
        list_rank: list[str] = rank.split(' ')

        for col, spot in enumerate(list_rank):
            md_board[line][col] += str.format(constants.board_spot, f"![]({constants.prefix}{constants.images[spot]})")

            if col == 7:
                md_board[line][col] += f"| {col - line + 1} |\n"
                md_board[line].insert(0, f'| {col - line + 1} ')

    s: str = ''.join([''.join(x) for x in md_board])

    text += f"{s}{constants.board_columns}"

    color_turn = constants.WHITE if utils.which_color_plays_board(board) is True else constants.BLACK
    hex_color = constants.HEX_WHITE if color_turn == constants.WHITE else constants.HEX_BLACK
    color = str.format(constants.color_str, color_turn, hex_color)
    text += f"{color}"

    for lm in legal_moves.keys():
        constants.legal_moves_str += f'| {lm} | {", ".join(legal_moves[lm])} |\n'
    constants.legal_moves_str += constants.legal_moves_str_end

    text += f"{constants.legal_moves_str}{constants.instructions}"

    md = open("chess.md", "w")
    md.write(text)
    md.close()
