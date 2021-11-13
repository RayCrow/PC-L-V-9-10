import hashlib
def encrypt_string(hash_string):
    sha_signature = \
                  hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'confidential data'
sha_signature = encrypt_string(hash_string)
print(sha_signature)

import hashlib
import os

path = input ("Escriba el nombre del archivo: ")

file_obj = open (path,"rb")
file = file_obj.read()

Hash = hashlib.sha512(file)
print(Hash)
Hashed = Hash.hexdigest()

print (Hashed)
