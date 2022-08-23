PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as name_list:
    names = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)


