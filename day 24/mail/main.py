PLACE_HOLDER ="[name]"

with open("./Input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input\Letters\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_names=name.strip()
        new_letter =letter_content.replace(PLACE_HOLDER,stripped_names)
        print(new_letter)

        with open (f"./Output/ReadyToSend/letter_for_{stripped_names}.txt",mode="w")as completted_letter:
            completted_letter.write(new_letter)