def selection_menu(default_or_not, WHITE_TOTAL=300, WHITE_INCRE=0, BLACK_TOTAL=300, BLACK_INCRE=0):
    # Choosing time and increment for the main run
    # Need to do args to get config at cli level
    if not default_or_not:
        print("Currently white's time and increment is {0} minutes with {1} seconds/move".format(int(WHITE_TOTAL/60), WHITE_INCRE))
        WHITE_TOTAL = input("Choose white's new total time: ")
        WHITE_INCRE = input("Choose white's new increment: ")

        print("Currently black's time and increment is {0} minutes with {1} seconds/move".format(int(BLACK_TOTAL/60), BLACK_INCRE))
        BLACK_TOTAL = input("Choose black's new total time: ")
        BLACK_INCRE = input("Choose black's new increment: ")

    output = [int(WHITE_TOTAL),int(WHITE_INCRE),int(BLACK_TOTAL),int(BLACK_INCRE)]
    return output
