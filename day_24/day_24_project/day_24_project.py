# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("day_24/day_24_project/Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.readlines()

with open("day_24/day_24_project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in list_of_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(
            f"day_24/day_24_project/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(new_letter)
