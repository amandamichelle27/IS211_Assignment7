#!/usr/bin/python2.7
from itertools import cycle
from random import randrange, seed
            
## Prompts the player for whether they want to continue rolling for the turn.
def should_continue():
    response = raw_input("Enter 'r' to continue rolling or 'h' to hold: ")
    if response not in ["r", "h"]:
        print "Invalid response."
        return should_continue()
    else:
        return response == "r"

class Player(object):
    def __init__(self):
        self.score = 0
    
class Die(object):
    def __init__(self, num_sides):
        self.num_sides = num_sides
        
    def roll(self, total_score, turn_score):
        result = randrange(1, self.num_sides + 1)
        print "You rolled a", result
        if result != 1:
            print "Your turn total is", turn_score + result
        print "Your total score is", total_score
        return result
        
class Game(object):
    def __init__(self, num_players=2, num_sides=6):
        self.players = [Player() for _ in range(num_players)]
        self.die = Die(num_sides)
        
    def play_game(self):
        for index, player in cycle(enumerate(self.players)):
            print "Is is now the turn for player", index
            turn_score = 0
            dice_roll = self.die.roll(player.score, turn_score);
            while dice_roll != 1:
                turn_score += dice_roll
                if not should_continue():
                    break
                dice_roll = self.die.roll(player.score, turn_score)
            if dice_roll != 1:
                player.score += turn_score
            if player.score >= 100:
                print "The winner was player", index
                break

if __name__ == "__main__":
    seed(0)
    Game().play_game()
