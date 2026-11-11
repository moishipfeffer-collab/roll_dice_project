from game import start_game,display_game_results,get_win_num
from storag import save_game,add_to_json

def show_menu():
    print("=======================")
    print("      ROLL DICE")
    print("=======================")
    while True:
        choise = input("1. Start new game\n2. View Game History\n" \
        "3. View Statistics\n4. Exit\n\nChoose an option: ")
        if choise in ["1","2","3","4"]:
            return choise
        print("\nnot valid choise, try again")

# option 1 play game

def start_game_flow(history:list):
    game = start_game()
    display_game_results(game)
    games = add_to_json(history,game)
    save_game(games)
    print("\nGame saved successfully!")

# option 2 view game history

def display_game_history(history:list):
    if not history:
        print("no games yet!")
    else:
        for game in history:
            print(f"\n----- GAME {history.index(game) + 1} -----\n\nplayer name: {game['player_name']}\n\
rounds: {game['rounds']}\nplayer_score: {game['player_score']}\n\
computer_score: {game['computer_score']}\nwinner: {game['winner']}\n\n")

# option 3 display_statistics

def display_statistics(history):
    print(f"\ngames number: {len(history)}")
    computer_winning = get_win_num(history,"computer")
    drow_game = get_win_num(history,"drow")
    player_winning = len(history) - computer_winning - drow_game
    print(f"player winning: {player_winning}")
    print(f"computer winning: {computer_winning}")
    print(f"drows: {drow_game}")
    print(f"winning percent:\nplayer: {player_winning / len(history) * 100}\n\
computer: {computer_winning / len(history) * 100}\ndrows: {drow_game / len(history) * 100}")



