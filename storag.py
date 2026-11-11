from pathlib import Path
import json 

games_file = Path(__file__).parent / "game_history.json"

def load_game_history():
    try:
        with open(games_file,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("the database is corrupted, starting empty")
        return []
    
def add_to_json(history,game):
    history.append(game)
    return history

def save_game(game):
    with open(games_file,"w") as file:
        json.dump(game,file,indent=4)