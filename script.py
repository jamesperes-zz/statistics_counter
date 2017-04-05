

def count(num):
    try:
        number = int(num)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        
    case_for_mouth = (number / 30)
    return number
