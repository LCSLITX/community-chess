title = "# Lucas's Community Chess\n\n"

instructions = f'''<details>\n<summary>Instructions</summary>\n\n\
If you are total beginner, you could learn more [here](https://en.wikipedia.org/wiki/Chess).\n\n
To move pieces, you need to know a little bit about, \
[chess notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)).\n\n
For simplicity reasons, this Chess game uses [UCI notation](https://en.wikipedia.org/wiki/Universal_Chess_Interface), which consist of: a square coordinate to move `FROM`; and a square coordinates to move `TO`.\n\
E.g.: To move from `a2` to `a4`, simply use `a2a4`.\n\n
You may consult what moves are available in Legal Moves.\
\n</details>'''

board_columns: str = '|   | A | B | C | D | E | F | G | H |   |\n'
board_div: str = '| - | - | - | - | - | - | - | - | - | - |\n'
board_spot: str = "| {0} "

prefix: str = 'https://raw.githubusercontent.com/LCSLITX/community-chess/66099ccc42252927be918eb729dd1b2224041dd9/assets/'

images: dict[str, str] = {
    # Black
    "r": "svg/r.svg",
    "n": "svg/n.svg",
    "b": "svg/b.svg",
    "q": "svg/q.svg",
    "k": "svg/k.svg",
    "p": "svg/p.svg",
    # White
    "R": "svg/R.svg",
    "N": "svg/N.svg",
    "B": "svg/B.svg",
    "Q": "svg/Q.svg",
    "K": "svg/K.svg",
    "P": "svg/P.svg",
    # Blank
    ".": "png/blank.png",
}

BLACK: str = "BLACK"
HEX_BLACK: str = "`#000000`"
WHITE: str = "WHITE"
HEX_WHITE: str = "`#ffffff`"

color_str = "\n\nNow it's **{0}** {1} turn."

legal_moves_str = f"\n\n<details>\n<summary>Legal Moves</summary>\n\n| from square | move to |\n| - | - |\n"
legal_moves_str_end = '\n</details>\n<br>\n'