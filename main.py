import chess

board = chess.Board()
fen = board.fen()

f = open("chess", "w")
f.write(fen)
f.close()
