import os
import sys


def read_banner(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def parse_banner(file_content):
    lower_bound = 32
    upper_bound = 126
    char_arts = file_content.split("\n\n")
    ascii_dict = {}

    for i, art in enumerate(char_arts):
        if i + lower_bound > upper_bound:
            break
        char_key = chr(i + lower_bound)
        ascii_dict[char_key] = art

    return ascii_dict

def generate_ascii_art(string_to_convert, ascii_dict, char_spacing=1, word_spacing=4):
    lines = string_to_convert.split("\n")
    ascii_art_lines = []
    character_width = max(len(line) for art in ascii_dict.values() for line in art.split("\n"))

    for line in lines:
        words = line.split(' ')
        ascii_art_for_line = ['' for _ in range(8)]

        for word_index, word in enumerate(words):
            for char in word:
                if char in ascii_dict:
                    char_art = ascii_dict[char].split("\n")
                    for i in range(8):
                        ascii_art_for_line[i] += char_art[i] + " " * char_spacing
                else:
                    for i in range(8):
                        ascii_art_for_line[i] += " " * character_width + " " * char_spacing

            if word_index < len(words) - 1:
                for i in range(8):
                    ascii_art_for_line[i] += " " * word_spacing

        ascii_art_lines.append("\n".join(ascii_art_for_line).rstrip())

    return "\n\n".join(ascii_art_lines)

def get_user_input():
    print("Welcome to the ASCII Art Generator!")
    string_to_convert = input("Enter the text to convert into ASCII art: ")
    string_to_convert = string_to_convert.replace("\\n", "\n")
    BANNER_TYPES = ['shadow', 'standard', 'thinkertoy']
    banner_type = input(f"Enter the banner type {BANNER_TYPES}: ").strip().lower()

    if banner_type not in BANNER_TYPES:
        print(f"Invalid banner type! Choose from {BANNER_TYPES}.")
        sys.exit(1)

    return string_to_convert, banner_type

def parse_arguments():
    BANNER_TYPES = ['shadow', 'standard', 'thinkertoy']
    args = sys.argv

    if len(args) < 2:
        print("Insufficient arguments provided.")
        print("Usage: python ascii_art_generator.py \"Your text here\" [banner_type] [char_spacing] [word_spacing]")
        sys.exit(1)

    string_to_convert = args[1].replace("\\n", "\n")

    if len(args) >= 3:
        banner_type = args[2].strip().lower()
        if banner_type not in BANNER_TYPES:
            print(f"Invalid banner type! Choose from {BANNER_TYPES}.")
            sys.exit(1)
    else:
        banner_type = 'standard'

    char_spacing = 1
    word_spacing = 4

    if len(args) >= 4:
        try:
            char_spacing = int(args[3])
            if char_spacing < 0:
                raise ValueError
        except ValueError:
            print("Error: Character spacing must be a non-negative integer.")
            sys.exit(1)

    if len(args) >= 5:
        try:
            word_spacing = int(args[4])
            if word_spacing < 0:
                raise ValueError
        except ValueError:
            print("Error: Word spacing must be a non-negative integer.")
            sys.exit(1)

    return string_to_convert, banner_type, char_spacing, word_spacing

def main():
    if len(sys.argv) > 1:
        if len(sys.argv) >= 5:
            string_to_convert, banner_type, char_spacing, word_spacing = parse_arguments()
        elif len(sys.argv) == 4:
            string_to_convert, banner_type, char_spacing, word_spacing = parse_arguments()
        else:
            string_to_convert, banner_type, char_spacing, word_spacing = parse_arguments()
    else:
        string_to_convert, banner_type = get_user_input()
        char_spacing = 1
        word_spacing = 4

    banner_path = f'./ascii_art/{banner_type}.txt'

    banner_content = read_banner(banner_path)
    ascii_dict = parse_banner(banner_content)
    ascii_art = generate_ascii_art(string_to_convert, ascii_dict, char_spacing, word_spacing)

    print("Generated ASCII Art:")
    print(ascii_art)

if __name__ == "__main__":
    main()
