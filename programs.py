
import random

def hangman():
    words = ["python", "hangman", "developer"]
    attempts = 6
    word = random.choice(words)
    guessed_letters = []

    while attempts > 0:
        display_text= ""
        for letter in word:
            if letter in guessed_letters:
                display_text += letter + " "
            else:
                display_text += "_ "

        print(display_text)
        
        guess = input("Guess the letter: ").lower()

        if len(guess) > 1:
            if guess == word:
                print("guessed correctly")
                break            
            else:
                attempts -= 1
                print(f'incorrect guess for the entire word, attempts left: {attempts}')
        
        if guess in guessed_letters:
            attempts -= 1
            print(f'already guessed the letter, {attempts} attempts left.')
            
        elif guess in word:
            print("correct guess!")
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print("You have guessed the entire word!")
                break

        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f'wrong guess {attempts} attempts left!')
    
    print("you have lost, good luck next time!")









import random

class tictactoe():
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = random.choice(["X","O"])


    def print_board(self):
        print("_" * 9)
        for row in self.board:
            print(" | ".join(row))
            print("_" * 9)

    def player_move(self):
        while True:
            try:
                row = int(input("Choose a row (0, 1, 2)"))
                col = int(input("Choose a column (0, 1, 2)"))
                if self.board[row][col] == " ":
                    self.board[row][col] = self.player
                    break
                elif self.board[row][col] != " ":
                    print("Position already taken!")
            except ValueError:
                print("Please pick a number between 0-2")
            except IndexError:
                print("dont pick a number thats not 0-2")


    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

    def check_winner(self):
        # row checking
        for row in self.board:
            if all(cell == self.player for cell in row):
                return True
        
        # Column checking
        for col in range(3):
            if all(self.board[row][col] == self.player for row in range(3)):
                return True
        
        #Diagonal checking
        if all(self.board[i][i] == self.player for i in range(3)) or all(self.board[i][2-i] == self.player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(cell != " " for row in self.board for cell in row)
    
    def play_game(self):
        while True:
            self.print_board()
            self.player_move()
            if self.check_winner():
                self.print_board()
                print(f'and the winner is {self.player}!')
                break
            elif self.check_tie():
                self.print_board()
                print("Its a tie")
                break
            self.switch_player()


game = tictactoe()
game.play_game()