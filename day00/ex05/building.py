import sys
import string


def count_characters(text: str) -> None:
    """Count and display the sums of different character types in a string."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    total = len(text)

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Main function to handle input and error cases."""
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument provided")

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        print("What is the text to count?")
        try:
            text = sys.stdin.read()
        except KeyboardInterrupt:
            text = input()

    count_characters(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
