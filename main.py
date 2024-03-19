import sys
import game


def main():
    args = len(sys.argv)
    move = None
    if args > 1:
        move = sys.argv[1]
    game.game(move)


if __name__ == "__main__":
    main()
