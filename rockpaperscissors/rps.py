import random
import sys


# use of class to define state
class RPS:
    def __init__(self):
        print("Welcome to RPS!")

        self.moves: dict = {"rock": "🪨", "scissors": "✂️", "paper": "📜"}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        user_move: str = input("Rock, paper, or scissors? >>").lower()
        if user_move == "exit":
            print("Exiting...")
            sys.exit()
        if user_move not in self.valid_moves:
            print("Invalid move...")
            return self.play_game()

        ai_move: str = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        print("----")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")

# Complete check_move
    def check_move(self, user_move: str, ai_move: str):
        ...


"""
An example using positional arguments and keyword arguments in functions
that contain dynamic parameters
"""
# def func(*args, **kwargs):
#     return f"Arguments: {args}, Keyword arguments: {kwargs}"


# params = [7, 10]
# options = {"c": False, "d": "world"}

# # res = func(*[7, 10], **{"c": False, "d": "world"})
# res = func(*params, **options)

# print("Type: ", type(res))

# print("Result: ", res)
