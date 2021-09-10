#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



display  =[]
for letter in range(len(chosen_word)):
    display.append("_")

end_of_game=False
while not end_of_game:

    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game= True
        print("You win")