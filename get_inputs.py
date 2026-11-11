from validations import check_empty,check_num

def get_name():
    while True:
        name = input("enter your name: ")
        if check_empty(name):
            return name 
        print("you dont have a name?")

def get_rounds_num(name):
    while True:
        rounds = input(f"{name}, how much rounds would you like (1-10) ? ")
        if not check_empty(rounds):
            print("number fan not be empty")
        if not check_num(rounds):
            print("rouns must be a number between 1-10")
        else:
            return int(rounds)
    