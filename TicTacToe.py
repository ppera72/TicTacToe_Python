import random


class TicTacToe:
    def __init__(self):
        self.rowA, self.rowB, self.rowC = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
        if random.randint(0, 1) == 0:
            self.player1, self.player2 = 'X', 'O'
        else:
            self.player1, self.player2 = 'O', 'X'
        self.player1Choices = []
        self.player2Choices = []
        self.availablePlaces = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        self.winningCombinations = (['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'],
                                    ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1'])
        print("Tic-Tac-Toe\nEnter - start the game\nQ - Quit the game")
        while True:
            decision = input()
            if decision == '':
                self.startGame()
                break
            elif decision.upper() == 'Q':
                self.quitGame()
            else:
                pass

    def grid(self):
        print("   1   2   3")
        print("A:", end="")
        for _ in self.rowA:
            print(f'[{_}] ', end="")

        print("\nB:", end="")
        for _ in self.rowB:
            print(f'[{_}] ', end="")

        print("\nC:", end="")
        for _ in self.rowC:
            print(f'[{_}] ', end="")
        print('\n')

    def gridChoice(self, player, choices):
        allowedChoices = {'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'}
        while True:
            choice = input(f'{player} input your choice: \n').upper()
            if choice in allowedChoices and choice in self.availablePlaces:
                choices.append(choice)
                self.availablePlaces.remove(choice)
                row, column = choice[0], int(choice[1])
                if row == "A":
                    self.rowA[column - 1] = player
                if row == "B":
                    self.rowB[column - 1] = player
                if row == "C":
                    self.rowC[column - 1] = player
                break
            else:
                print("Invalid place, try another one!")

    def checkWinner(self, choices):
        for winningRows in self.winningCombinations:
            if all([item in choices for item in winningRows]):
                return True
        return False

    def startGame(self):
        print(f'Player 1: {self.player1} | Player 2: {self.player2}')
        print("You choose a grid with: A3, B2, A1 etc.")
        while self.availablePlaces:
            self.grid()
            self.gridChoice(self.player1, self.player1Choices)
            if len(self.player1Choices) == 5 and not self.checkWinner(self.player1Choices):
                print("\nDraw!")
                self.grid()
                TicTacToe()
            if self.checkWinner(self.player1Choices):
                print(f'\n{self.player1} wins!')
                self.grid()
                TicTacToe()
            self.grid()
            self.gridChoice(self.player2, self.player2Choices)
            if self.checkWinner(self.player2Choices):
                print(f'\n{self.player2} wins!')
                self.grid()
                TicTacToe()

    @staticmethod
    def quitGame():
        quit("Thanks for playing! :)")


def main():
    TicTacToe()


if __name__ == "__main__":
    main()
