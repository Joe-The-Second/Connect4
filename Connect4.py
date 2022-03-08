board = [
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ",
    " ", " ", " ", " ", " ", " ", " ",
    "P", "P", "P", "P", "P", "P", "P",
    "P", "P", "P", "P", "P", "P", "P",
    "P", "P", "P", "P", "P", "P", "P",
    "P", "P", "P", "P", "P", "P", "P",
    "P", "P", "P", "P", "P", "P", "P",
    "P", "P", "P", "P", "P", "P", "P"]

turn = "R"
playing = True

def print_board(board):
    print(board[0], "|", board[1], "|", board[2], "|", board[3], "|", board[4], "|", board[5], "|", board[6])
    print(board[7], "|", board[8], "|", board[9], "|", board[10], "|", board[11], "|", board[12], "|", board[13])
    print(board[14], "|", board[15], "|", board[16], "|", board[17], "|", board[18], "|", board[19], "|", board[20])
    print(board[21], "|", board[22], "|", board[23], "|", board[24], "|", board[25], "|", board[26], "|", board[27])
    print(board[28], "|", board[29], "|", board[30], "|", board[31], "|", board[32], "|", board[33], "|", board[34])
    print(board[35], "|", board[36], "|", board[37], "|", board[38], "|", board[39], "|", board[40], "|", board[41])


def player_turn(board):
    print_board(board)
    inp = int(input("Insert 1 for the first collum, and so on until collum 6: "))
    global turn
    if inp == 1:
        for i in range(35, -1, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 2:
        for i in range(36, 0, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 3:
        for i in range(37, 1, -7):
            if board[i] == " " :
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 4:
        for i in range(38, 2, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 5:
        for i in range(39, 3, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 6:
        for i in range(40, 4, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break
    if inp == 7:
        for i in range(41, 5, -7):
            if board[i] == " ":
                board[i] = turn
                if turn == "R":
                    turn = "Y"
                elif turn == "Y":
                    turn = "R"
                break


def player_win(board):
    global playing
    global turn
    for e in range(0, 42, 7):
        for i in range(e, e + 7):
            if board[i] != " ":
                if board[6 + e] == board[7 + e]:
                    break
                if board[i] == board[i + 1] == board[i + 2] == board[i + 3]:
                    if turn == "R":
                        print("Winner is Yellow")
                        playing = False
                    elif turn == "Y":
                        print("Winner is Red")
                        playing = False
    for e in range(0, 42):
        for i in range(e, e + 22, 7):
            if board[i] != " ":
                if board[6 + e] == board[7 + e]:
                    break
                if board[i] == board[i + 7] == board[i + 14] == board[i + 21] and board[i] != "P":
                    while playing:
                        if turn == "R":
                            print("Winner is Yellow")
                            playing = False
                        elif turn == "Y":
                            print("Winner is Red")
                            playing = False
    for e in range(0, 42):
        for i in range(e, e + 25, 8):
            if board[i] != " ":
                if board[6 + e] == board[7 + e]:
                    break
                if board[i] == board[i + 8] == board[i + 16] == board[i + 24] and board[i] != "P":
                    while playing:
                        if turn == "R":
                            print("Winner is Yellow")
                            playing = False
                        elif turn == "Y":
                            print("Winner is Red")
                            playing = False
    for e in range(0, 42):
        for i in range(e, e + 19, 6):
            if board[i] != " ":
                if board[i] == board[i + 6] == board[i + 12] == board[i + 18] and board[i] != "P":
                    while playing:
                        if turn == "R":
                            print("Winner is Yellow")
                            playing = False
                        elif turn == "Y":
                            print("Winner is Red")
                            playing = False


while playing:
    player_win(board)
    player_turn(board)