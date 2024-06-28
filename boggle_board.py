import random

class BoggleBoard:
  def __init__(self):
    print("----\n----\n----\n----\n")


  def shake(self):
    board = ''

    for i in range(16):
      for j in range(6):
        random_letter = BoggleBoard.generate_random_letter()
        if random_letter == "Qu":
          board += random_letter + " "
          random_letter = BoggleBoard.generate_random_letter()
        else:
          board += random_letter + "  "
          random_letter = BoggleBoard.generate_random_letter()
      board += "\n"
    print(board)


  def generate_random_letter():
    random_letter = (chr(random.randint(97, 121))).upper()
    return random_letter if random_letter != 'Q' else 'Qu'
