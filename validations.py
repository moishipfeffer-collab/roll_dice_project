def check_empty(input):
    if input.strip():
        return True
    return False

def check_num(num):
    try:
        return 11 > int(num) > 0
    except:
        return False
