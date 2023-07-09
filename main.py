import secrets
import string
import base64
import hashlib

from cryptography.fernet import Fernet

def encrypt():
    choice = int(input("Enter the menu number below:\n1. Use your own key\n:2. Use new key from system\n "))
    if choice == 1:
        # opening the key
        user_key = input("key for decrypt:?\n")
        key = user_key

        # using the key from user input
        fernet = Fernet(key)

        # change the 'asd.pdf' file to your file
        # opening the original file to encrypt
        with open('asd.pdf', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and writing the encrypted data
        with open('asd-enc.pdf', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print("encrypt succeed!\n\n")

    elif choice == 2:
        # opening the key
        with open('filekey.txt', 'rb') as filekey:
            key = filekey.read()

        # using the generated key from function generate_key function
        fernet = Fernet(key)

        # change the 'asd.pdf' file to your file
        # opening the original file to encrypt
        with open('asd.docx', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('asd-enc.docx', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print("encrypt succeed!\n\n")


def decrypt():
    # opening the key
    user_key = input("key for decrypt:?\n")
    key = user_key

    # using the key
    fernet = Fernet(key)

    # change the 'asd-enc.pdf' file to your file
    # opening the encrypted file
    with open('asd-enc.pdf', 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open('asd-enc-dec.pdf', 'wb') as dec_file:
        dec_file.write(decrypted)
    print("decrypt succeed!\n\n")



def generate_key():
    # key generation
    key = Fernet.generate_key()
    # insert the key in a file
    with open('filekey.txt', 'wb') as filekey:
        filekey.write(key)
        print("The key is already saved to your directory as 'filekey.txt' :)\n")

def hash():
    # change the 'asd.docx' file to your file
    with open('asd.docx', 'rb') as enc_file:
        encrypted = enc_file.read()

    # sha256Hash value is converted to hexadecimal to make it easier to be processed
    sha256Hash = hashlib.sha256(encrypted)
    sha256Hashed = sha256Hash.hexdigest()

    sha384Hash = hashlib.sha384(encrypted)
    sha384Hashed = sha384Hash.hexdigest()

    sha3_256_Hash = hashlib.sha3_256(encrypted)
    sha3_256_Hashed = sha3_256_Hash.hexdigest()

    sha512Hash = hashlib.sha512(encrypted)
    sha512Hashed = sha512Hash.hexdigest()

    blake2bHash = hashlib.blake2b(encrypted)
    blake2bHashed = blake2bHash.hexdigest()

    print("SHA-256 Hash (256-bits): " + sha256Hashed)
    print("SHA-384 Hash (384-bits): " + sha384Hashed)
    print("SHA-3 Hash (256-bits): " + sha3_256_Hashed)
    print("SHA-512 Hash (512-bits): " + sha512Hashed)
    print("Blake2 Hash (512-bits): " + blake2bHashed + "\n")

def password_generator():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    user_input_password = int(input("Password length? "))
    password_length = user_input_password

    if password_length < 8 or password_length > 64:
        print("Password length cannot be below 8 or exceed 64.\n")
        password_generator()

    else:
        password = ''.join(secrets.choice(alphabet) for _ in range(password_length))
        print(password, "\n")

def title(text, color):
    """
    Prints the specified text in the specified color.
    """
    color_code = {
        "green": "\033[32m",
        "yellow": "\033[33m",
    }
    reset_code = "\033[0m"

    if color.lower() in color_code:
        print(color_code[color.lower()] + text + reset_code)
    else:
        print(text)


# print title
title("-----------------------------", "yellow")
title("|        LIGHTHOUSE         |", "green")
title("-----------------------------", "yellow")

while True:
    menu = int(input("Menu\n"
                     "1.Encrypt \n"
                     "2.Decrypt \n"
                     "3.Encryption key\n"
                     "4.Hash\n"
                     "5.Password Generator\n"
                     "0.exit\n"
                     "please enter the menu number: "))
    if menu == 1:
        encrypt()

    elif menu == 2:
        decrypt()

    elif menu == 3:
        generate_key()

    elif menu == 4:
        hash()

    elif menu == 5:
        password_generator()

    elif menu == 0:
        print("\nThank you for using us!")
        break

    else:
        print("Enter the available menu only!")
