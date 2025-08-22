def play_turn(game_board: list, x: int, y: int, piece: str):
  if x >= 3 or y >= 3:
    return False
  if game_board[y][x] != "":
    return False
  game_board[y][x] = piece
  return True
