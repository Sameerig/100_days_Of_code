alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def  caesar(text, shift , direction):
    cipher=""
    if direction=="encode":
        for letter in text:
            position =alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher=cipher+new_letter
        print(f"The encoded text is {cipher}")

    elif direction=="decode":
        for word in text:
            location = alphabet.index(word)
            simple_position = location - shift
            simple_text = alphabet[simple_position]
            cipher= cipher+simple_text
        print(f"The without cipher text is {cipher}")


caesar(text=text,shift=shift, direction=direction)