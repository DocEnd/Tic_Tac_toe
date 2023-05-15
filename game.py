from turtle import Turtle
from random import choice

SCREEN_COLOR = '#00BFFF'

class Game_title(Turtle):
    def __init__(self):
        super(Game_title,self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.title = "TIC TAC TOE!"

    def write_initial_title (self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 150)
        self.write(self.title, align="center", font=('Courier', 25, 'bold'))

    def change_title(self, new_title):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 150)
        self.write(new_title, align="center", font=('Courier', 25, 'bold'))

class Score_board(Turtle):
    def __init__(self):
        super(Score_board,self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")

    def write_score(self, player_x_score, player_o_score):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-150,200)
        self.write(f"X Score: |{player_x_score}|", align="center", font=('Courier', 20, 'bold'))
        self.goto(150, 200)
        self.write(f"O Score: |{player_o_score}|", align="center", font=('Courier', 20, 'bold'))

class Text_writing(Turtle):
    def __init__(self):
        super(Text_writing,self).__init__()
        self.hideturtle()
        self.penup()

    def write_text(self, text_input):
        self.write(text_input, align="center", font=('Courier', 25, 'bold'))

    def write_text_down(self, text_input):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0,-200)
        self.write_text(text_input)

class Game_element(Turtle):
    def __init__(self):
        super(Game_element,self).__init__()
        self.hideturtle()
        self.penup()

    def place_at_position(self,x_cor,y_cor):
        self.setposition(x=x_cor,y=y_cor)

    def start_element(self):
        self.shape("square")
        self.turtlesize(3,3,12)
        self.color("white")
        self.showturtle()

    def x_element(self):
        self.shape("x_black.gif")
        self.color("black")
        self.showturtle()

    def o_element(self):
        self.shape("o_black.gif")
        self.color("black")
        self.showturtle()

    def x_win_element(self):
        self.shape("x_green.gif")

    def o_win_element(self):
        self.shape("o_green.gif")

class Game_process(Turtle):
    def __init__(self):
        super(Game_process,self).__init__()
        self.hideturtle()
        self.score_player_x=0
        self.score_player_o=0
        self.winning_combinations = {
            1: ["1_1","1_2","1_3"],
            2: ["2_1","2_2","2_3"],
            3: ["3_1","3_2","3_3"],
            4: ["1_1","2_1","3_1"],
            5: ["1_2", "2_2", "3_2"],
            6: ["1_3", "2_3", "3_3"],
            7: ["1_1", "2_2", "3_3"],
            8: ["1_3", "2_2", "3_1"]
        }
        self.goes_next = None
        self.coordinates = {
    '1_1':{
        'x_min': -130,
        'x_center':-100,
        'x_max': -70,
        'y_min': 70,
        'y_center':100,
        'y_max':130,
        },
    '1_2':{
        'x_min': -30,
        'x_center':0,
        'x_max': 30,
        'y_min': 70,
        'y_center':100,
        'y_max':130,
        },
    '1_3': {
        'x_min': 70,
        'x_center': 100,
        'x_max': 130,
        'y_min': 70,
        'y_center': 100,
        'y_max': 130,
    },
    '2_1':{
        'x_min': -130,
        'x_center':-100,
        'x_max': -70,
        'y_min': -30,
        'y_center':0,
        'y_max':30,
        },
    '2_2':{
        'x_min': -30,
        'x_center':0,
        'x_max': 30,
        'y_min': -30,
        'y_center':0,
        'y_max': 30
    },
    '2_3': {
        'x_min': 70,
        'x_center': 100,
        'x_max': 130,
        'y_min': -30,
        'y_center':0,
        'y_max': 30,
    },
    '3_1': {
        'x_min': -130,
        'x_center': -100,
        'x_max': -70,
        'y_min': -130,
        'y_center': -100,
        'y_max': -70,
    },
    '3_2': {
        'x_min': -30,
        'x_center': 0,
        'x_max': 30,
        'y_min': -130,
        'y_center': -100,
        'y_max': -70,
    },
    '3_3': {
        'x_min': 70,
        'x_center': 100,
        'x_max': 130,
        'y_min': -130,
        'y_center': -100,
        'y_max': -70,
    }
}
        self.start_dictionary_elements = {}
        self.game_dictionary_elements = {}
        self.x_list = []
        self.o_list = []
        self.next_place = None
        self.winner = None
        self.title_writer = Game_title()
        self.writer = Text_writing()
        self.score_writer = Score_board()
        self.game_type = None
        self.win_comb_nr = None

    def ask_nr_of_players(self):
        asking = True
        while asking:
            nr_players = int(self.screen.textinput("HELLO", "How many players?\n(1 - To play with Computer \n 2 - To play with Player):"))
            if 1 <= nr_players <= 2 or nr_players == 2:
                asking = False
                self.game_type = nr_players

    def setup_screen(self):
        self.screen.title("TIC-TAC-TOE Game!")
        self.screen.setup(500, 500)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.addshape(name="x_black.gif", shape=None)
        self.screen.addshape(name="x_red.gif", shape=None)
        self.screen.addshape(name="x_green.gif", shape=None)
        self.screen.addshape(name="o_black.gif", shape=None)
        self.screen.addshape(name="o_red.gif", shape=None)
        self.screen.addshape(name="o_green.gif", shape=None)

    def play_game(self):

        self.screen.clear()
        self.setup_screen()

        self.title_writer.write_initial_title()
        self.score_writer.write_score(self.score_player_x, self.score_player_o)
        self.put_start_elements_on_the_board()
        self.appreciate_first_player()
        if self.game_type == 2:
            self.screen.onclick(self.play_the_2_players_game)
        elif self.game_type == 1:

            self.screen.onclick(self.play_the_1_player_game)


    def put_start_elements_on_the_board (self):
        self.winner = None
        for place in self.coordinates:
            new_element = Game_element()
            new_element.start_element()
            new_element.place_at_position(x_cor=self.coordinates[place]["x_center"],y_cor=self.coordinates[place]["y_center"])

            self.start_dictionary_elements[place] = new_element
        self.screen.update()


    def appreciate_first_player(self):
        self.winner=None
        variants = ["x", "o"]
        result = choice(variants)
        self.goes_next = result
        self.writer.write_text_down(f"First is '{self.goes_next.upper()}'")
        return self.goes_next

    def change_player(self):
        if self.goes_next == "x" and self.winner == None:
            self.goes_next ="o"
            self.writer.write_text_down(f"Next move is '{self.goes_next.upper()}'")
            return self.goes_next
        elif self.goes_next == "o" and self.winner == None:
            self.goes_next ="x"
            self.writer.write_text_down(f"Next move is '{self.goes_next.upper()}'")
            return self.goes_next

    def get_next_place_on_board(self,x,y):
        for place in self.coordinates:
            if self.coordinates[place]["x_min"]<= x <=self.coordinates[place]["x_max"] \
                    and self.coordinates[place]["y_min"]<= y <=self.coordinates[place]["y_max"]:
                self.next_place = place
                return self.next_place

    def check_if_free_space(self, place):
        # If the clicked place is in the Game directory means that it is not free so no place to put new element
        if place in self.game_dictionary_elements:
            return False
        else:
            return True

    def check_winner(self, list, player_symbol:str):
        if len(self.game_dictionary_elements) <= 9:
            for combination in self.winning_combinations:
                nr_of_coincidence = 0
                for element in self.winning_combinations[combination]:
                    if element in list:
                        nr_of_coincidence += 1

                    if nr_of_coincidence > 2:
                        self.winner = player_symbol.lower()
                        self.win_comb_nr = combination
                        self.color_winner_combination()
                        if self.winner == "x":
                            self.score_player_x+=1
                            text_to_write = f"{self.winner.upper()} Player Wins!!!"
                            self.writer.write_text_down(text_to_write)
                        elif self.winner == "o":
                            self.score_player_o+=1
                            text_to_write = f"{self.winner.upper()} Player Wins!!!"
                            self.writer.write_text_down(text_to_write)
                            self.score_writer.write_score(self.score_player_x, self.score_player_o)
                    elif self.winner == None and len(self.game_dictionary_elements) == 9:
                        text_to_write = "No one Wins! It's a Tie!"
                        self.writer.write_text_down(text_to_write)
                        self.winner = "tie"

        if self.winner != None:
            contiue_play = self.ask_play_more()
            if contiue_play:
                self.play_game()

            else:
                self.writer.write_text_down("THE END!")
                self.title_writer.change_title(f'Thank you for playing!')
                self.score_writer.write_score(self.score_player_x,self.score_player_o)
                self.screen.exitonclick()

    def play_the_2_players_game(self, x,y):
        place = self.get_next_place_on_board(x,y)
        if place is not None and self.check_if_free_space(place):
            if self.goes_next == "x":
                new_element = Game_element()
                new_element.x_element()
                new_element.place_at_position(x_cor=self.coordinates[place]["x_center"], y_cor=self.coordinates[place]["y_center"])
                self.game_dictionary_elements[place] = new_element
                self.x_list.append(place)
                self.x_list.sort()
                self.check_winner(self.x_list,self.goes_next.upper())
                self.change_player()

            elif self.goes_next == "o":
                new_element = Game_element()
                new_element.o_element()
                new_element.place_at_position(x_cor=self.coordinates[place]["x_center"],
                                              y_cor=self.coordinates[place]["y_center"])
                self.game_dictionary_elements[place] = new_element
                self.o_list.append(place)
                self.o_list.sort()
                self.check_winner(self.o_list,self.goes_next.upper())
                self.change_player()

    def play_the_1_player_game(self, x, y):
        if self.goes_next == 'x':
            self.player_move(x,y)
        elif self.goes_next == 'o':
            self.computer_move()

    def list_from_dict(self, the_dict):
        list = []
        for elem in the_dict:
            list.append(elem)
        return list

    def computer_move(self):
        list =self.list_from_dict(self.start_dictionary_elements)
        no_right_choice = True
        while no_right_choice:
            place = choice(list)
            if place is not None and self.check_if_free_space(place):
                no_right_choice=False
                new_element = Game_element()
                new_element.o_element()
                new_element.place_at_position(x_cor=self.coordinates[place]["x_center"],
                                              y_cor=self.coordinates[place]["y_center"])
                self.game_dictionary_elements[place] = new_element
                self.o_list.append(place)
                self.o_list.sort()
                self.check_winner(self.o_list, self.goes_next.upper())
                self.change_player()

    def player_move(self, x, y):
        place = self.get_next_place_on_board(x,y)
        if place is not None and self.check_if_free_space(place):
            new_element = Game_element()
            new_element.x_element()
            new_element.place_at_position(x_cor=self.coordinates[place]["x_center"], y_cor=self.coordinates[place]["y_center"])
            self.game_dictionary_elements[place] = new_element
            self.x_list.append(place)
            self.x_list.sort()
            self.check_winner(self.x_list,self.goes_next.upper())
            self.change_player()

    def ask_play_more(self):
        answer = None
        while answer != True or answer != False:
            question = self.screen.textinput("Hello dear Player", "Do you want to play more?(y/n):").lower()
            if question == "y":
                self.start_dictionary_elements = {}
                self.game_dictionary_elements = {}
                self.x_list=[]
                self.o_list=[]
                answer = True
                return answer
            elif question == "n":
                answer = False
                return answer

    def color_winner_combination(self):
        if self.winner == "x":
            for element in self.winning_combinations[self.win_comb_nr]:
                self.game_dictionary_elements[element].x_win_element()
        elif self.winner == "o":
            for element in self.winning_combinations[self.win_comb_nr]:
                self.game_dictionary_elements[element].o_win_element()
