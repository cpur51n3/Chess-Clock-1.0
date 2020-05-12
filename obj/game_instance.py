import time as t
import os, sys
from pynput import keyboard

class game:
    def __init__(self,WT=300,WI=0,BT=300,BI=0):
        # Set default white and black time params
        self.WHITE_TOTAL = WT
        self.BLACK_TOTAL = BT
        self.WHITE_INCRE = WI
        self.BLACK_INCRE = BI
        self.game_on = False
        self.white_move = False
        self.black_move = False
        self.listener = keyboard.Listener(on_press=self.keyboard_listen)
        self.listener.start()

    def start_game(self): # The main logic for timing
        input("Press enter whenever you are ready to start the game")
        # Starting Game
        self.game_on = True
        self.white_move = True
        while self.game_on:
            t.sleep(0.97)
            if self.white_move == True:
                self.WHITE_TOTAL = self.time_countdown(self.WHITE_TOTAL,self.WHITE_INCRE)
                self.terminal_display()
            elif self.black_move == True:
                self.BLACK_TOTAL = self.time_countdown(self.BLACK_TOTAL,self.BLACK_INCRE)
                self.terminal_display()

            if self.BLACK_TOTAL == 0:
                self.game_on = False
                print("Black Timed Out")
            elif self.WHITE_TOTAL == 0:
                self.game_on = False
                print("White Timed Out")

    def time_countdown(self,time,increment):
        # Function to count down from time to 0 and send return to signal
        time = time - 1
        return time

    def time_increment(self,time,increment):
        # Incrementing - adding more time
        print("Added {} seconds".format(increment))
        time = time + increment + 1 # Additional second to account for the time_countdown of the action
        return time

    def terminal_display(self):
        os.system("cls")
        # print("White has {} seconds left".format(self.WHITE_TOTAL))
        # print("Black has {} seconds left".format(self.BLACK_TOTAL))
        print("White: {}:{:02d} \nBlack: {}:{:02d}".format(
                                                    int(self.WHITE_TOTAL/60),
                                                    int(self.WHITE_TOTAL%60),
                                                    int(self.BLACK_TOTAL/60),
                                                    int(self.BLACK_TOTAL%60))
                                                    )

    def keyboard_listen(self,key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        if k == 'left':  # keys of interest
            print('White\'s move')
            if not self.white_move:
                self.WHITE_TOTAL = self.time_increment(self.WHITE_TOTAL,self.WHITE_INCRE)
                # self.BLACK_TOTAL = self.BLACK_TOTAL + 1
            self.white_move = True
            self.black_move = False
        elif k == 'right':
            print('Black\'s move')
            if not self.black_move:
                self.BLACK_TOTAL = self.time_increment(self.BLACK_TOTAL,self.BLACK_INCRE)
                # self.WHITE_TOTAL = self.WHITE_TOTAL + 1
            self.black_move = True
            self.white_move = False
