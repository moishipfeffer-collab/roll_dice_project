import random
from get_inputs import get_rounds_num,get_name

def roll_dice():
    return random.randint(1,6)

def calc_winner(computer,player):
    if computer > player:
        winner = "computer"
    elif player > computer:
        winner = "player"
    else:
        winner = "drow"
    return winner

def play_round():
    computer = roll_dice()
    input("pres enter to play your turn: ")
    player = roll_dice()
    winner = calc_winner(computer,player)
    print(f"computer: {computer}, player: {player}, winner: {winner}")
    return {"round":None,"player_dice":player,"copueter_dice":computer,"winner":winner}

def display_game_results(game):
    print("===================")
    print("    NEW GAME")
    print("===================")
    print(f"player name: {game['player_name']}")
    print(f"number of rounds: {game['rounds']}")
    for i in range(game['rounds']):
        print(f"---------- ROUND {i+1} ----------\n{game['player_name']}: {game['results'][i]['player_dice']}\n \
        comuter: {game['results'][i]['copueter_dice']}\n\n{game['results'][i]['winner']} \
        wins this round!")
    print("====================")
    print("     GAME OVER")
    print("====================")
    print(f"{game['player_name']}: {game['player_score']}")
    print(f"computer: {game['computer_score']}\n")
    print(f"WINNER: {game['winner']}!")



def start_game():
    player_score = 0
    computer_score = 0
    player_name = get_name()
    round_num = 0
    results = []
    rounds = get_rounds_num(player_name)
    for i in range(rounds):
        round_num += 1
        round_res = play_round()
        round_res["round"] = round_num
        if round_res["winner"] == "player":
            player_score += 1
        elif round_res["winner"] == "computer":
            computer_score += 1
        results.append(round_res)
    winner = calc_winner(computer_score,player_score)
    if winner == "player":
        winner = player_name
    return {"player_name":player_name,"rounds":round_num,"player_score":player_score,
    "computer_score":computer_score,"winner":winner,"results":results}


def get_win_num(history,type):
    count = 0
    for game in history:
        if game['winner'] == type:
            count += 1
    return count

