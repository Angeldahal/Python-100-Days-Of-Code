from unittest import result
def encrypt_decrypt(given_text,shift_amount,operation):
    result_text=""
    for letter in given_text:
        position = alphabet.index(letter)
        if operation == "encode":
            new_letter = alphabet[position+shift_amount]
            result_text += new_letter
        elif operation == "decode":
            new_letter = alphabet[position - shift_amount]
            result_text += new_letter
    print(f"The result string after is {result_text} ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run = "yes"
while run=="yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #Don't change the code above 👆

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    # def encrypt(plain_text, shift_amount): 
    #   cipher_text = ""
    #   for letter in plain_text:
    #     position = alphabet.index(letter)
    #     new_position = position + shift_amount
    #     new_letter = alphabet[new_position]
    #     cipher_text += new_letter
    #   print(f"The encoded text is {cipher_text}")

    # def decrypt(cipher_text, shift_amount):
    #     original_text = ""
    #     for letter in cipher_text:
    #         position = alphabet.index(letter)
    #         new_position = position - shift_amount
    #         new_letter = alphabet[new_position]
    #         original_text += new_letter
    #     print(f"The decoded text is {original_text}")
    
    encrypt_decrypt(text,shift,direction)
    run = input("Enter yes to run again")