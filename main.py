def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

# This line calls your main function when the program runs
if __name__ == "__main__":
    main()