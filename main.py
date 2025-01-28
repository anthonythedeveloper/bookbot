def main():
    # Open and read the contents of the file
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        # Get the word count
        word_count = word_counting(file_contents)

        # Get the character count
        character_count = downsizer(file_contents)

        # Print the report
        print_report(character_count, word_count)

def word_counting(text):
    # Split text into words and count them
    words = text.split()
    return len(words)

def downsizer(text):
    # Count characters (case insensitive) using a dictionary
    character_count = {}
    for character in text:
        # Convert to lowercase
        lower_character = character.lower()

        # Include only alphabetic characters
        if lower_character.isalpha():
            if lower_character in character_count:
                character_count[lower_character] += 1
            else:
                character_count[lower_character] = 1

    return character_count

def print_report(character_count, word_count):
    # Print the beginning banner
    print("--- Begin report of books/frankenstein.txt ---")

    # Print the word count
    print(f"{word_count} words found in the document\n")

    # Convert character count dictionary into a sorted list of dictionaries
    sorted_character_count = sorted(
        [{"character": char, "count": count} for char, count in character_count.items()],
        key=lambda x: x["count"],
        reverse=True
    )

    # Print each character count in sorted order
    for item in sorted_character_count:
        print(f"The '{item['character']}' character was found {item['count']} times")

    # Print the ending banner
    print("\n--- End report ---")

# Run the script
if __name__ == "__main__":
    main()
