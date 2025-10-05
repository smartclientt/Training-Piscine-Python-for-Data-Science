import sys
import string


def count_characters(text: str) -> None:
    """Count and display the sums of different character types in a string."""
    # Initialize counters
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    # Calculate total
    total = len(text)

    # Print results
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Main function to handle input and error cases."""
    # Check number of arguments
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument provided")

    # Get text from argument or input
    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        try:
            # Read until EOF (Ctrl+D)
            text = sys.stdin.read()
        except KeyboardInterrupt:
            # If Ctrl+D not used, fall back to input()
            text = input()

    # Count and display character types
    count_characters(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
