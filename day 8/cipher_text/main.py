from art import logo

print(logo)


def cipher(text, shift,direction):
    position =""
    if direction=="encode":
        for letter in text:
            text_location= alphabets.index(letter)
            new_location = text_location+ shift
            position= position+alphabets[new_location]
        print(f"Your cipher text is {position}")
    elif direction=="decode":
        for letter in text:
            text_location= alphabets.index(letter)
            new_location = text_location- shift
            position= position+alphabets[new_location]
        print(f"Your cipher text is {position}")
    else:
        print("Sorry you are giving us the wrong command!")
    
    
from art import logo
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

should_continue=True
while should_continue:
    direction = input("Enter encode for encoding and decode for decoding:")
    message = input("Enter the message: ")
    shift_amount=int(input("Enter the shift value: "))
    # encode(message,shift_amount)
    shift_amount=shift_amount%25
    cipher(message,shift_amount,direction)

    result =input("type yes if you want to go again else no: ")
    if result=="no":
        should_continue=False
        print("good bye")