import cryptography
from cryptography.fernet import Fernet

def main():
    print("Michael Gallagher Module 2 Assignment")

    print("Option 1 - Syncronous Key Generation")
    print("Option 2 - Syncronous Key Encryption")
    print("Option 3 - Syncronous Key Decryption")

    choice = input()

    if choice == "1":
        generate_sync_key()
    elif choice == "2":
        s_encrypt()
    elif choice == "3":
        s_decrypt()
        

def generate_sync_key():
    print("Generating key")
    key = Fernet.generate_key()
    print(key.decode("utf-8")) #We use .decode in order to convert from a bytes option


def get_key_stdin():
    key_text = input().strip()
    key = key_text.encode("utf-8")
    return key


def s_encrypt():
    print("Please enter your key")
    key = get_key_stdin()
    print(key)
    text = input("Enter the text to encrypt")

def s_decrypt():
    pass

main()
