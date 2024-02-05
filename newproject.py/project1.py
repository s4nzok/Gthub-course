
def get_number():
    return int(input("what is the number?"))
        

def main():
    x = get_number()
    if is_even(x):
        print("even")
    else:
        print("odd")    
def is_even(n):
    return True if n % 2 == 0 else False

main()