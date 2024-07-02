import random

class BoggleBoard:
  def __init__(self):
    self.boggle_board = [
      "AAEEGN",
      "ELRTTY",
      "AOOTTW",
      "ABBJOO",
      "EHRTVW",
      "CIMOTU",
      "DISTTY",
      "EIOSST",
      "DELRVY",
      "ACHOPS",
      "HIMNQU",
      "EEINSU",
      "EEGHNW",
      "AFFKPS",
      "HLNNRZ",
      "DEILRX"
    ]
    print("----\n----\n----\n----\n")


  def shake(self):
    random_numbers_arr = self.get_random_nums(16, 4)
    boggle_board = ''

    for i in range(len(random_numbers_arr)):
      random_numbers_arr_two = self.get_random_nums(6, 4)
      list_of_letters = list(self.boggle_board[random_numbers_arr[i]])

      for j in random_numbers_arr_two:
        letter = list_of_letters[j]
        
        if letter == 'Q':
          boggle_board += "Qu "
        else:
          boggle_board += f"{letter}  "
      boggle_board += "\n"
    return boggle_board


  def get_random_nums(self, num, length):
    input_nums = range(0,num)
    random_numbers = random.sample(input_nums,length)
    return random_numbers

