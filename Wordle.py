from pathlib import Path
word_file = Path("5-letter-words.txt")

def load_word_bank():
    if word_file.exists():
        return word_file
    else:
        print(" Error - File not found! :( ")

#Using a reference document approach
def load_word_bank (filename = "5-letter-words.txt"):
    with open(filename, "r") as file:
        return [line.strip().lower() for line in file if len(line.strip()) == 5]

word_bank = load_word_bank()

def main():
    print("Wordle Test Project")
    # Using the word_file call on a random element in the file