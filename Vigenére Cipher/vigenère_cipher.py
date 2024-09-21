def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(text, key):
    encrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
            encrypted_text.append(chr(shift + ord('A') if text[i].isupper() else shift + ord('a')))
        else:
            encrypted_text.append(text[i])
    return "".join(encrypted_text)

def vigenere_decrypt(text, key):
    decrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].upper()) - ord(key[i].upper())) % 26
            decrypted_text.append(chr(shift + ord('A') if text[i].isupper() else shift + ord('a')))
        else:
            decrypted_text.append(text[i])  # Harf değilse olduğu gibi ekle
    return "".join(decrypted_text)


def main():
    print("--- Vigenère Cipher ---")
    
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        
        # Kullanıcıdan işlem seçimi
        choice = input("Select an option (1/2): ")

        if choice == '1':
            text = input("Message: ")
            key = input("Key: ")
            key = generate_key(text, key)
            encrypted_text = vigenere_encrypt(text, key)
            print(f"Encrypted Message: {encrypted_text}")
            break
        elif choice == '2':
            text = input("Message: ")
            key = input("Key: ")
            key = generate_key(text, key)
            decrypted_text = vigenere_decrypt(text, key)
            print(f"Decrypted Message: {decrypted_text}")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
