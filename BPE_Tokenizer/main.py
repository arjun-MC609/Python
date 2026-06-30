"""
main.py
-------

Command-line interface for the BPE tokenizer.
"""

from tokenizer import BPETokenizer


def menu():

    print("\n========== BPE TOKENIZER ==========")
    print("1. Train Tokenizer")
    print("2. Encode Text")
    print("3. Decode Token IDs")
    print("4. Show Vocabulary")
    print("5. Show Merge Rules")
    print("6. Show Statistics")
    print("7. Exit")
    print("==================================")

    return input("Choice: ").strip()


def train(tokenizer):

    tokenizer.load_dataset()
    tokenizer.train()


def encode(tokenizer):

    text = input("\nText: ")

    ids = tokenizer.encode(text)

    print("\nToken IDs:")
    print(ids)


def decode(tokenizer):

    text = input("\nToken IDs (space separated): ")

    try:
        ids = [int(x) for x in text.split()]
    except ValueError:
        print("Invalid token IDs.")
        return

    result = tokenizer.decode(ids)

    print("\nDecoded Text:")
    print(result)


def vocabulary(tokenizer):

    limit = input("Maximum entries (default=50): ").strip()

    if limit:
        tokenizer.print_vocab(int(limit))
    else:
        tokenizer.print_vocab()


def merges(tokenizer):

    limit = input("Maximum rules (default=50): ").strip()

    if limit:
        tokenizer.print_merges(int(limit))
    else:
        tokenizer.print_merges()


def statistics(tokenizer):

    tokenizer.statistics()


def main():

    tokenizer = BPETokenizer()

    while True:

        choice = menu()

        if choice == "1":

            train(tokenizer)

        elif choice == "2":

            encode(tokenizer)

        elif choice == "3":

            decode(tokenizer)

        elif choice == "4":

            vocabulary(tokenizer)

        elif choice == "5":

            merges(tokenizer)

        elif choice == "6":

            statistics(tokenizer)

        elif choice == "7":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
