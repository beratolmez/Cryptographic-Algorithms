def caesar_encrypt(text, shift):
    result = ""
    
    for char in text:
        # For uppercase
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # For lowercase
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Not a letter
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    print("--- CAESAR CIPHER ---")
    print("Select the encryption method you want to use:\n1. Encrypt\n2. Decrypt\n3. Exit")
    choice = 0
    while choice > 3 or choice <= 0:
        choice = int(input("Option (1/2/3): "))

        if choice == 1:
            text = input("Enter the text to be encrypted: ")
            shift = int(input("Shift value: "))
            encrypted_text = caesar_encrypt(text, shift)
            print(f"Crypted message: {encrypted_text}")

        elif choice == 2:
            text = input("Enter the text to be decrypted: ")
            shift = int(input("Shift value: "))
            decrypted_text = caesar_decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")
        
        elif choice == 3:
            print("Have a good day!")

        else:
            print("You have selected an invalid option. Please enter a valid value.")

if __name__ == "__main__":
    main()