# Import and print the logo from art.py when the program starts
from art_caesar import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    # Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt():
        if direction == 'encode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
         # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet
            # by the shift amount and print the encrypted text.
            encrypted_text = ""
            for letter in text:
             if letter in alphabet:
                 shifted_letter = chr((ord(letter) + shift - 97) % 26 + 97)
                 encrypted_text += shifted_letter
             else:
                 encrypted_text += letter
            print(f"Your encrypted message is: {encrypted_text}")

    # Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
    def decrypt():
        if direction == 'decode':
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypted_text = ""
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the
    # shift amount and print the decrypted text.
            for letter in text:
              if letter in alphabet:
                shifted_letter = chr((ord(letter) - shift - 97) % 26 + 97)
                decrypted_text += shifted_letter
              else:
                  decrypted_text += letter
            print(f"Your decrypted message is: {decrypted_text}")

    #Create a function called caesar() to combine encrypt, decrypt, direction
    def caesar():
        if direction == 'encode':
            encrypt()
        elif direction == 'decode':
            decrypt()

    caesar()

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_end = True
        print("Have a nice day!")