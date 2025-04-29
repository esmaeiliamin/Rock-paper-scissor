import random


class RockPaperScissors:
    """Main class for Rock, Paper, Scissors game"""
    def __init__(self, name: str):
        self.player_name = name
        self.choices = ["rock", "paper", "scissors"]

    def get_player_choice(self):
        """Get the users choice"""
        user_choice = input(f'Enter your choice ({self.choices}):')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        else:
            print("Invalid choice. You must choose rock, paper, or scissors.")
            return self.get_player_choice()

    def get_computer_choice(self):
        """Get computer choice randomly from the choices list"""
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        """Decide the winner of the game based on the choices of the user and computer

        Args:
            user_choice (str): The choice of the user
            computer_choice (str): The choice of the computer

        Returns:
            str: The winner of the game
        """
        if user_choice == computer_choice:
            return "It's a Tie!"
        win_combinations = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
        for combo in win_combinations:
            if (user_choice == combo[0]) & (computer_choice == combo[1]):
                return "Congratulations! You win!"
        return "Sorry! You lose!"

    def play(self):
        """Play the game of Rock, Paper, Scissors"""
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        print(f"{self.player_name} chose {user_choice}")
        print(f"Computer chose {computer_choice}")
        print(f"{winner} wins!")


if __name__ == "__main__":
    game = RockPaperScissors('Amin')

while True:
    game.play()

    continue_game = input('Do you want to play again? (y/n): ')
    if continue_game == 'y':
        continue
    else:
        break
print('Thanks for playing!')
