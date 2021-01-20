from Cryptodome.Cipher import DES, AES, ARC2, Blowfish
from cryptography.fernet import Fernet
import random
import base64


def pad(text, length):
    while len(text) % length != 0:
        text += ' '
    return text

def generate_key(length):
    key = random.randint(0, pow(2, length)-1)
    f = open("key.txt", "w")
    f.write(str(key))
    f.close()
    return key




def switch_func_encrypt(hash,message):
    return {
        'des': lambda message : encrypt_DES(message),
        'aes': lambda message : encrypt_AES(message),
        'arc2': lambda message : encrypt_ARC2(message),
        'blowfish': lambda message : encrypt_blowfish(message),
        'fernet': lambda message : encrypt_fernet(message),
    }.get(hash)(message)


def encrypt(algo=''):
    try:
      print('Enter your message to encrypt with',algo, 'algorithm:\n')
      message = input()
      print('\nThe result is : \n',switch_func_encrypt(algo,message))     
      message = input('\nEnter anything to exit :\n')
    except:
      print("\nAn exception occurred do you want to retry?") 
      answer ='0'      
      while answer =='0':
            answer = input('y/n:\n')
            if answer == "y":
                print("\nRetrying...\n") 
                encrypt()
            elif answer == "n":
                print('\nThanks for using, goodbye.')
                exit
            else:
                print("I don't understand your choice.")
                answer='0'

def switch_func_decrypt(hash, message, key):
    return {
        'des': lambda message : decrypt_DES(message, int(key)),
        'aes': lambda message : decrypt_AES(message, int(key)),
        'arc2': lambda message : decrypt_ARC2(message, int(key)),
        'blowfish': lambda message : decrypt_blowfish(message, int(key)),
        'fernet': lambda message : decrypt_fernet(message, key),
    }.get(hash)(message)

def decrypt(algo=''):
    try:
      print('Enter your message to decrypt with',algo, 'algorithm:\n')
      message = input()
      print('\nEnter the key : \n')
      key = input()
      print('\nThe result is : \n',switch_func_decrypt(algo,message, key))
      message = input('\nEnter anything to exit :\n')
    except:
      print("\nAn exception occurred do you want to retry?")
      answer ='0'      
      while answer =='0':
            answer = input('y/n:\n')
            if answer == "y":
                print("\nRetrying...\n") 
                decrypt()
            elif answer == "n":
                print('\nThanks for using, goodbye.')
                exit
            else:
                print("I don't understand your choice.")
                answer='0'


# DES algorithm
def encrypt_DES(message):
    key = generate_key(8)
    key_bytes = key.to_bytes(8, 'big')
    des = DES.new(key_bytes, DES.MODE_ECB)
    pad_string = pad(message, 8).encode('utf8')
    crypt = des.encrypt(pad_string)
    return base64.b64encode(crypt).decode('utf8'), key

def decrypt_DES(encrypted_message, key):
    key_bytes = key.to_bytes(8, 'big')
    des = DES.new(key_bytes, DES.MODE_ECB)
    encrypted_message = base64.b64decode(encrypted_message.encode())
    return des.decrypt(encrypted_message).decode('utf8')


# AES algorithm

def encrypt_AES(message):
    key = generate_key(16)
    key_bytes = key.to_bytes(16, 'big')
    aes = AES.new(key_bytes, AES.MODE_ECB)
    pad_string = pad(message, 16).encode('utf8')
    crypt = aes.encrypt(pad_string)
    return base64.b64encode(crypt).decode('utf8')

def decrypt_AES(encrypted_message, key):
    key_bytes = key.to_bytes(16, 'big')
    aes = AES.new(key_bytes, AES.MODE_ECB)
    encrypted_message = base64.b64decode(encrypted_message.encode())
    return aes.decrypt(encrypted_message).decode('utf8')



# ARC2 algorithm

def encrypt_ARC2(message):
    key = generate_key(16)
    key_bytes = key.to_bytes(16, 'big')
    arc2 = ARC2.new(key_bytes, ARC2.MODE_ECB)
    pad_string = pad(message, 16).encode('utf8')
    crypt = arc2.encrypt(pad_string)
    return base64.b64encode(crypt).decode('utf8')

def decrypt_ARC2(encrypted_message, key):
    key_bytes = key.to_bytes(16, 'big')
    arc2 = ARC2.new(key_bytes, AES.MODE_ECB)
    encrypted_message = base64.b64decode(encrypted_message.encode())
    return arc2.decrypt(encrypted_message).decode('utf8')



#Blowfish algorithm


def encrypt_blowfish(message):
    bs = Blowfish.block_size
    key = generate_key(bs)
    key_bytes = key.to_bytes(bs, 'big')
    blowfish = Blowfish.new(key_bytes, Blowfish.MODE_ECB)
    pad_string = pad(message, 16).encode('utf8')
    crypted = blowfish.encrypt(pad_string)
    return base64.b64encode(crypted).decode('utf8')

def decrypt_blowfish(encrypted_message, key):
    bs = Blowfish.block_size
    key_bytes = key.to_bytes(bs, 'big')
    blowfish = Blowfish.new(key_bytes, AES.MODE_ECB)
    encrypted_message = base64.b64decode(encrypted_message.encode())
    return blowfish.decrypt(encrypted_message).decode('utf8')


#Fernet algorithm

def encrypt_fernet(message):
    key = Fernet.generate_key().decode('utf8')
    f = open("key.txt", "w")
    f.write(str(key))
    f.close()
    fernet = Fernet(key)
    pad_string = pad(message, 16).encode('utf8')
    return  fernet.encrypt(pad_string).decode('utf8')

def decrypt_fernet(encrypted_message, key):
    key = key.encode()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode('utf8')

