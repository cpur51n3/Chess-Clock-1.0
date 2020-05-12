import time as t
import os, sys
import json
from pynput import keyboard
# Internal dependencies
from obj.game_instance import game
from obj.lib.selection_menu import selection_menu as selection_menu

def main():
    with open("presets.json", 'r') as file1:
        data = file1.read()
        presets = json.loads(data)
    try:
        defaults_or_not = input("Quick Game - (5 minutes, no increments)? (y for yes/p for presets/c for custom time): ").lower()
        if defaults_or_not == "y":
            run_obj = game()
            run_obj.start_game()
        elif defaults_or_not == "c":
            new_times = selection_menu(False)
            run_obj = game(new_times[0],new_times[1],new_times[2],new_times[3])
            run_obj.start_game()
        elif defaults_or_not == "p":
            print("Available preset times: ")
            for item in presets:
                print(f"Game mode: {item}")
            while True:
                preset_choice = input("Your choice: ")
                if preset_choice in presets.keys():
                    run_obj = game(presets[preset_choice][0],presets[preset_choice][1],presets[preset_choice][2],presets[preset_choice][3])
                    run_obj.start_game()
                    break
                else:
                    print("That was not one of the options")
    except KeyboardInterrupt:
        run_obj.game_on = False
        print("Game has ended")
    except:
        print("There was a problem starting the game")
    try:
        del run_obj
    except:
        pass

if __name__ == "__main__":
    main()
    print("Thanks for using the chess clock!")
