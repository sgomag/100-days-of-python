# Get a list with guests' names
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    list_of_guests = names_file.readlines()

# Get starting_letter's content
with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()

# Create new file for each guest
for name in list_of_guests:
    stripped_name = name.strip("\n")
    new_letter = letter_contents.replace("[name]", stripped_name)
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)