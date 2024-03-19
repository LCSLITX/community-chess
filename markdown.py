import chess
import constants


def render_md(board: chess.Board) -> None:
    """This function receives a board and render it in a markdown file.
    :param board: An instantiated board.
    :type board: chess.Board
    :return: None
    """
    md_board: list[list] = [["" for _ in range(8)] for _ in range(8)]  # creates a 8x8 array

    b: str = board.__str__()
    ranks: list[str] = b.splitlines()

    for i, rank in enumerate(ranks):
        rank: list[str] = rank.split(' ')

        for j, spot in enumerate(rank):
            if spot == " ":
                continue

            md_board[i][j] += str.format(constants.board_spot, f"![]({constants.prefix}{constants.images[spot]})")

            if j == 7:
                md_board[i][j] += f"| {j - i + 1} |\n"
                md_board[i].insert(0, f'| {j - i + 1} ')

    s: str = ''.join([''.join(x) for x in md_board])

    text: str = f"{constants.board_columns}\n{constants.board_div}\n{s}{constants.board_columns}"
    md = open("chess.md", "w")
    md.write(text)
    md.close()
