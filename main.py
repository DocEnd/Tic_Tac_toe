from game import Game_process
from turtle import Screen

SCREEN_COLOR = '#00BFFF'

screen = Screen()


# Game PROCESSOR:
game_processor = Game_process()

game_processor.setup_screen()
game_processor.ask_nr_of_players()

game_processor.play_game()

screen.mainloop()