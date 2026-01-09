#basic encryption algorithm
print("Welcome to the basic encryption program!")
print("Enter the text you want to encrypt:")
user_input = input(str).lower()
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char == " ":
            encrypted_text += " "  # Preserve spaces
        elif chr(ord(char) + 13) > 'z':
            encrypted_text += chr((ord(char) - 13) - 26).lower()  # Wrap around the alphabet
        else:    
            encrypted_text += chr(ord(char) + 13).lower()  # Shift character by 13
    return encrypted_text
print("Encrypted text:", encrypt(user_input))
