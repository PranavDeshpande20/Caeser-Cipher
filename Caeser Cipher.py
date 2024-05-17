import string
letters = string.ascii_lowercase

operation = int(input("Choose a operation: 1) Encrypt\n                    2) Decrypt\nType in the number:"))
user_input = input("Enter text: ")
user_shift = int(input("Enter the shift value: "))
user_input = user_input.lower()

def encrypt(input_str,shift):
    encrypted_text = ""
    for char in input_str:
        new_index = (letters.index(char) + shift) % 26
        encrypted_text += letters[new_index]
    print("Encrypted Text: " + encrypted_text)

def decrypt(input_str,shift):
    decrypted_text = ""
    for char in input_str:
        new_index = (letters.index(char) - shift) % 26
        decrypted_text += letters[new_index]
    print("Decrypted Text: " + decrypted_text)
 
if operation == 1:
    encrypt(user_input,user_shift)
elif operation == 2:
    decrypt(user_input,user_shift)
else:
    print("Enter a valid number.")
    
    