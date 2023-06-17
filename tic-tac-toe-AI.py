import random
import winsound

# variables
tic_tac_toe_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player_score = 0
ai_score = 0
game_on = True
global turn
player_beep_sound_frequency = 2500
ai_beep_sound_frequency = 1500
board_full_beep_sound_frequency = 500
beep_sound_duration = 500


# Scroll to bottom for game start code

def playerTurn():
    # getting user play
    play = input('Your play: ')
    while type(play) != int:
        try:
            if 0 <= int(play) <= 9:
                # converting user input to int (1 - 9), since the program
                # has gotten the right input to end the while loop
                play = int(play)
                # calling update table function
                updateTable(players_dict['player'], play)
                # printing out game board with verified user play
                print(
                    f"{tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}\n-----------\n{tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]} \n-----------\n{tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}")
                # beep for user play
                winsound.Beep(player_beep_sound_frequency, beep_sound_duration)
        # while the player input is not the desired input (number 1 to 9)
        # keep asking for right input
        except ValueError:
            play = input('Wrong input! Your play can only be a number from 1 to 9: ')


def aiTurn():
    # ai generates are random play from 1 to 9 inclusive
    ai_play_position = random.randint(1, 9)
    # calling updateTable function with ai generated number and storing result in variable
    ai_play_position = updateTable(players_dict['ai'], ai_play_position)
    # printing ai choice after program verification from updateTable function
    print(f"Computers Play: {ai_play_position}")
    # printing updated table with ai play
    print(
        f"{tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}\n-----------\n{tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]} \n-----------\n{tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}")
    # beep sound for ai play
    winsound.Beep(ai_beep_sound_frequency, beep_sound_duration)


def checkIfPositionAlreadyUsed(play):
    # if positions 1,2,3(index 0,1,2) are empty return 'good'
    if play <= 3:
        if tic_tac_toe_board[0][play - 1] == ' ':
            return 'Good'
    # if positions 4,5,6(index 3,4,5) are empty return 'good'
    elif play <= 6:
        # we take away 4 because the indexes can only be from [0][0] to [2][2]
        # hence if play is 6 for example
        # [1][play - 4] will give [1][6 - 4] = [1][2] (row 2,column 3)
        # (row 2,column 3) is position 6 on the board
        if tic_tac_toe_board[1][play - 4] == ' ':
            return 'Good'
    # if positions 7,8,9(index 6,7,8) are empty return 'good'
    elif play <= 9:
        if tic_tac_toe_board[2][play - 7] == ' ':
            return 'Good'
    # if postion is not empty, nothing is returned


def updateTable(player_icon, play_position):
    # checking to see if postition is available
    if checkIfPositionAlreadyUsed(play_position) == 'Good':
        # if position is available, game table will be updated with the appropriate icon
        if play_position <= 3:
            tic_tac_toe_board[0][play_position - 1] = player_icon
        elif play_position <= 6:
            tic_tac_toe_board[1][play_position - 4] = player_icon
        elif play_position <= 9:
            tic_tac_toe_board[2][play_position - 7] = player_icon
        # if ai is playing, ai play position will be returned since the program
        # has confirmed that the ai's choice is available
        if turn == 'ai':
            return play_position

    # if the position is already taken
    else:
        # if the user is playing
        if turn == 'player':
            # asking user for a different input
            play_position = int(input('Position has already been used. Please enter another position: '))
            # function recursion, trying to update game board with new user play
            updateTable(player_icon, play_position)
        else:
            # if ai is playing
            # ai will pick a different position
            play_position = random.randint(1, 9)
            # calling update table function again with new ai position and storing in variable
            ai_play = updateTable(player_icon, play_position)
            # if program gets to this point it means new ai position is available
            # returning new ai position to aiturn function
            return ai_play


def isThereAWinner():
    # X Winning horizontally
    if (tic_tac_toe_board[0][0] == 'X' and tic_tac_toe_board[0][1] == 'X' and tic_tac_toe_board[0][2] == 'X') or (
            tic_tac_toe_board[1][0] == 'X' and tic_tac_toe_board[1][1] == 'X' and tic_tac_toe_board[1][2] == 'X') or (
            tic_tac_toe_board[2][0] == 'X' and tic_tac_toe_board[2][1] == 'X' and tic_tac_toe_board[2][2] == 'X'):
        return True
    # X Winning vertically
    elif (tic_tac_toe_board[0][0] == 'X' and tic_tac_toe_board[1][0] == 'X' and tic_tac_toe_board[2][0] == 'X') or (
            tic_tac_toe_board[0][1] == 'X' and tic_tac_toe_board[1][1] == 'X' and tic_tac_toe_board[2][1] == 'X') or (
            tic_tac_toe_board[0][2] == 'X' and tic_tac_toe_board[1][2] == 'X' and tic_tac_toe_board[2][2] == 'X'):
        return True
    # X Winning horizontally
    elif (tic_tac_toe_board[0][0] == 'X' and tic_tac_toe_board[1][1] == 'X' and tic_tac_toe_board[2][2] == 'X') or (
            tic_tac_toe_board[0][2] == 'X' and tic_tac_toe_board[1][1] == 'X' and tic_tac_toe_board[2][0] == 'X'):
        return True
    # O Winning horizontally
    elif (tic_tac_toe_board[0][0] == 'O' and tic_tac_toe_board[0][1] == 'O' and tic_tac_toe_board[0][2] == 'X') or (
            tic_tac_toe_board[1][0] == 'O' and tic_tac_toe_board[1][1] == 'O' and tic_tac_toe_board[1][2] == 'O') or (
            tic_tac_toe_board[2][0] == 'O' and tic_tac_toe_board[2][1] == 'O' and tic_tac_toe_board[2][2] == 'O'):
        return True
    # O Winning vertically
    elif (tic_tac_toe_board[0][0] == 'O' and tic_tac_toe_board[1][0] == 'O' and tic_tac_toe_board[2][0] == 'O') or (
            tic_tac_toe_board[0][1] == 'O' and tic_tac_toe_board[1][1] == 'O' and tic_tac_toe_board[2][1] == 'O') or (
            tic_tac_toe_board[0][2] == 'O' and tic_tac_toe_board[1][2] == 'O' and tic_tac_toe_board[2][2] == 'O'):
        return True
    # O Winning horizontally
    elif (tic_tac_toe_board[0][0] == 'O' and tic_tac_toe_board[1][1] == 'O' and tic_tac_toe_board[2][2] == 'O') or (
            tic_tac_toe_board[0][2] == 'O' and tic_tac_toe_board[1][1] == 'O' and tic_tac_toe_board[2][0] == 'O'):
        return True
    # if there is no winner return false
    else:
        return False


def isPlayingBoardFull():
    # setting initial board status to true
    board_status = True
    # looping through board to check if any space is left
    for row in tic_tac_toe_board:
        for position in row:
            # if empty space is found return false (board is not full)
            if position == ' ':
                board_status = False
                return board_status
    # if no empty space is found, return initial board status value (true)
    # it is true that playing board is full
    return board_status


def boardFullRestart():
    # beeping twice for when board is full
    for i in range(0, 2):
        winsound.Beep(board_full_beep_sound_frequency, beep_sound_duration)
    # asking user if they wish to play again
    play_again = input('No more moves left to make. Would you like to start over? Y or N: ').upper()
    # keep asking for desired input if wrong input is given
    while (play_again != 'Y') and (play_again != 'N'):
        play_again = input('Sorry you gave the wrong input! Would you like to start over? Y or N: ').upper()
    # ending game if they don't wish to keep playing
    if play_again == 'N':
        print('Thanks for playing!')
        # setting game_on variable to false which ends the game
        global game_on
        game_on = False
    else:
        # if player wishes to continue playing
        # board is cleared out
        global tic_tac_toe_board
        tic_tac_toe_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        print(
            f"{tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}\n-----------\n{tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]} \n-----------\n{tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}")


def winnerFoundRestart():
    # asking user if they wish to play again since winner has been found
    play_again = input('Would you like to play again? Y or N: ').upper()
    # keep asking for desired input if wrong input is given
    while (play_again != 'Y') and (play_again != 'N'):
        play_again = input('Sorry you gave the wrong input! Would you like to play again? Y or N: ').upper()
    # ending game if they don't wish to keep playing
    if play_again == 'N':
        print('Thanks for playing!')
        # setting game_on variable to false which ends the game
        global game_on
        game_on = False
    else:
        # if player wishes to continue playing
        # board is cleared out
        global tic_tac_toe_board
        tic_tac_toe_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        print(
            f"{tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}\n-----------\n{tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]} \n-----------\n{tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}")


# MAIN GAME CODE

print('Welcome to the tic tac toe game!')

# asking user to pick an icon
player_icon_choice = input('are you X or O? ').upper()

# Keep asking player for input until right input is given (x or 0)
while (player_icon_choice != 'X') and (player_icon_choice != 'O'):
    player_icon_choice = input('Sorry you gave the wrong input! are you X or O? ').upper()

# assigning game icon to player and ai based on player choice
if player_icon_choice == 'X':
    players_dict = {'player': 'X', 'ai': 'O'}
    print('Great choice! you are X for the game')
else:
    players_dict = {'ai': 'X', 'player': 'O'}
    print('Great choice! you are O for the game')

print("The rule of the game is to place your chosen icon in the range of 1 to 9! You're playing against AI. Have Fun!")
print(f"1 | 2 | 3\n-----------\n4 | 5 | 6\n-----------\n7 | 8 | 9")

# game will keep going until player chooses to end the game
while game_on:
    # player turn to play
    turn = 'player'
    playerTurn()
    # program will proceed to check for a winner after player turn
    # if there is no winner, program checks if there is space on the
    # board for the game to continue
    if not isThereAWinner():
        if isPlayingBoardFull():
            # if there is no space on the board
            # game will restart with player confirmation
            boardFullRestart()
        # if there is still space on the board
        # ai turn to play
        turn = 'ai'
        aiTurn()
        # program will proceed to check for a winner after ai turn
        # if there is no winner, program checks if there is space on the
        # board for the game to continue
        if isThereAWinner():
            # if there is a winner, it means ai has won the game
            # since ai was the last to play
            ai_score += 1
            print(f"{players_dict['ai']} Wins! Better luck next time!")
            print(f'winner: AI {ai_score}')
            print(f'loser: You {player_score}')
            # ai winning sound is played twice
            for i in range(0, 2):
                winsound.Beep(ai_beep_sound_frequency, beep_sound_duration)
            # restarting game with user confirmation since a winner was found
            winnerFoundRestart()
        # if there was no winner after ai played, program checks if there is space on the
        # board for the game to continue
        if isPlayingBoardFull():
            boardFullRestart()
    # if there is a winner after player has played, it means the
    # player(human) has won the game
    else:
        player_score += 1
        print(f"{players_dict['player']} Wins! Great Job!")
        print(f'winner: You {player_score}')
        print(f'loser: AI {ai_score}')
        # player winning sound is played twice
        for i in range(0, 2):
            winsound.Beep(player_beep_sound_frequency, beep_sound_duration)
        winnerFoundRestart()
