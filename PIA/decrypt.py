from cryptography.fernet import Fernet
import os
import argparse

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)

def main(path_to_encrypt):
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    key = cargar_key()
    decrypt(full_path, key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.
                                RawDescriptionHelpFormatter)

    parser.add_argument("-dec", metavar='DESENCRIPTAR', dest="dec", required=True)

    main()

