# !/usr/bin/python

# this is the script for decrypting

#firstly import the liblary to encrypt project
from os import remove
from sys import argv
from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def key_gen(passwd):
    # convert passwd to bytes
    passwd = passwd.encode('utf-8')
    # create a random salt from os
    salt = b'\xd1\xafy\x8d\xd1/\xa1Pv4\xea\xf1-1\xe0~\xb2$\x17D\xdd\xa7\x8fwrmd\x02\x7f`f:'
    # create kdf instance
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # derive an key prom the passwd
    key = urlsafe_b64encode(kdf.derive(passwd))
    #return key
    return key

def decrypt_file(file_path, passwds):
    # read data from the file
    try:
        with open (file_path, 'rb') as original:
            original_content = original.read()
    except FileNotFoundError:
        print('File not Found!')
        exit()

    for passwd in passwds:
        # this is the decryption script
        key = key_gen(passwd) # generate the key
        fernet_obj = Fernet(key) # create fernet obj
        original_content = fernet_obj.decrypt(original_content)

    #before saving the file remove old file
    remove(file_path)
    # write encrypted data
    with open(file_path, 'wb') as decrypted:
        decrypted.write(original_content)


def main():
    file_path = argv[1].strip()
    passwds = argv[2:]

    if len(argv) < 3 or argv[1] == '--help' or argv[1] == '-h':
        print('Usage: decrypt [file] [passwords]')
    else:
        # call the decrption function
        decrypt_file(file_path, passwds)

if __name__ == '__main__':
    main()