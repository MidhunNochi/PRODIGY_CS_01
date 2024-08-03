def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice in ['E', 'D']:
            break
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
