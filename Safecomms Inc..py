import random

def generate_key():
    return list(range(95))  

def encrypt_message(message):
    key = generate_key()
    random.shuffle(key)
    encrypted = []
    for char in message:
        if 32 <= ord(char) <= 126: 
            index = ord(char) - 32
            encrypted.append(f"{key[index]:02d}")
        else:
            encrypted.append('XX')  
    return ''.join(encrypted) + ''.join(f"{k:02d}" for k in key)

def decrypt_message(encrypted_message):
    message_part = encrypted_message[:-190] 
    key_part = encrypted_message[-190:]  
    key = [int(key_part[i:i+2]) for i in range(0, 190, 2)]
    decryption_map = {f"{v:02d}": chr(i + 32) for i, v in enumerate(key)}
    
    decrypted = []
    for i in range(0, len(message_part), 2):
        chunk = message_part[i:i+2]
        if chunk == 'XX':
            decrypted.append(' ')
        else:
            decrypted.append(decryption_map.get(chunk, ' '))
    return ''.join(decrypted)


while True:
    choice = input("Do you want to (e)ncrypt, (d)ecrypt, or (q)uit? ").strip().lower()

    if choice == 'e':
        message = input("Enter your message to encrypt: ")
        encrypted = encrypt_message(message)
        print("Encrypted message:", encrypted)

    elif choice == 'd':
        encrypted_message = input("Enter your encrypted message: ")
        decrypted = decrypt_message(encrypted_message)
        print("Decrypted message:", decrypted)

    elif choice == 'q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
