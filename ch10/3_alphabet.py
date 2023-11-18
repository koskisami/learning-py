def sortwords(file_path="words.txt"):
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]
            sortedwords = sorted(words)
            print("Words in an alphabetical order:")
            for word in sortedwords:
                print(word)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    sortwords()