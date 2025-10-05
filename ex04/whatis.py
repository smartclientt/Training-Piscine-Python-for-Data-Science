import sys

def main():
    """Check if a number is odd or even."""
    # Check number of arguments
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 1:
        return
    
    # Try to convert argument to integer
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    # Check if odd or even
    print("I'm Even." if num % 2 == 0 else "I'm Odd.")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")