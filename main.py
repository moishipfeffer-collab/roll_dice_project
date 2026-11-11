from run_app import show_menu,start_game_flow,display_game_history,display_statistics
from storag import load_game_history
def main():
    while True:
        history = load_game_history()
        choise = show_menu()
        if choise == "1":
            start_game_flow(history)
        elif choise == "2":
            display_game_history(history)
        elif choise == "3":
            display_statistics(history)
        elif choise == "4":
            break
main()
