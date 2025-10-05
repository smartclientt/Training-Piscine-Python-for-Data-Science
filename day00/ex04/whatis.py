import sys

def main():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        return
    
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    print("I'm Even." if num % 2 == 0 else "I'm Odd.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")