import hashlib, sys, time
from itertools import product


def switch_func(hash,message):
    return {
        'md5': lambda message : md5(message),
        'sh1': lambda message : sh1(message),
        'sha256': lambda message : sha256(message),
        'sha384': lambda message : sha384(message),
        'sha512': lambda message : sha512(message),
        'ripemd_160': lambda message : ripemd_160(message),
    }.get(hash)(message)


def hashage(hash=''):
    try:
      print('Enter your message to hash with',hash, ':\n')
      message = input()
      print('\nThe result is : \n',switch_func(hash,message))     
      message = input('\nEnter anything to exit :\n')
    except:
      print("\nAn exception occurred do you want to retry?") 
      answer ='0'      
      while answer =='0': 
            answer = input('y/n:\n')
            if answer == "y":
                print("\nRetrying...\n") 
                hashage()
            elif answer == "n":
                print('Thanks for using, goodbye.')
                exit
            else:
                print("I don't understand your choice.")
                answer='0'



def md5(message):
    hashMD5 = hashlib.md5(message.encode('ascii'))
    return hashMD5.hexdigest()


def sh1(message):
    hashSHA1 = hashlib.sha1(message.encode())
    return hashSHA1.hexdigest()

def sha256(message):
    hashSHA256 = hashlib.sha256(message.encode())
    return hashSHA256.hexdigest()

def sha384(message):
    hashSHA384 = hashlib.sha384(message.encode())
    return hashSHA384.hexdigest()

def sha512(message):
    hashSHA512 = hashlib.sha512(message.encode())
    return hashSHA512.hexdigest()

def ripemd_160(message):
    hashRIPEMD_160 = hashlib.new('ripemd160')
    hashRIPEMD_160.update(message.encode('ascii'))
    return hashRIPEMD_160.hexdigest()



def get_algorithm( type ):
    # Dynamically creates the right function and returns it
    # using python closure, it is only used to build types_dict
    def algorithm( string ):
        h = type()
        h.update(string.encode('utf-8'))
        return h.hexdigest()
    return algorithm


TYPES_DICT = { 32 : get_algorithm( hashlib.md5 ),
               40 : get_algorithm( hashlib.sha1 ),
               56 : get_algorithm( hashlib.sha224 ),
               64 : get_algorithm( hashlib.sha256 ),
               96 : get_algorithm( hashlib.sha384 ),
               128 : get_algorithm( hashlib.sha512 ) }



class Crackhash( object ):
    
    def __init__( self ):
        self.decrypt_method = None
        self.decrypted_hash = None
        self.user_file = None

    def dictionary_attack_call(self,dictionary_name):
        self.user_hash = self.get_hash()
        while self.decrypted_hash == None:
            self.wordlist = self.gen_wordlist(dictionary_name) # get the wordlist...
            self.decrypted_hash = self.dict_attack()                

            if self.decrypted_hash != None: # if hash_check returns a match carry out the 2 lines below and end the program
                self.elapsed = (time.time() - self.start) # This is the time taken to find a match.
                print('Hash cracked in '+str(self.elapsed)+' seconds. The correct word is: \n'+self.decrypted_hash)
                message = input('\nEnter anything to exit :\n')
            else:
                self.retry('no matches found')
            

   
    def brute_force_call(self):
        self.user_hash = self.get_hash()
        while self.decrypted_hash == None:
            self.decrypted_hash = self.brute_force()
            if self.decrypted_hash != None: # if hash_check returns a match carry out the 2 lines below and end the program
                self.elapsed = (time.time() - self.start) # This is the time taken to find a match.
                print('Hash cracked in '+str(self.elapsed)+' seconds. The correct word is: \n'+self.decrypted_hash)
                message = input('\nEnter anything to exit :\n')
            else:
                self.retry('no matches found')
            
 

    def get_hash(self):
        while True:
            hash_input = input('Please enter the hash:\n')

            if hash_input.isalnum(): # Ensures that the hash only contains alpha-numeric characters
                length = len(hash_input)
                
                if TYPES_DICT.get( length, None ):
                    self.hashtype = TYPES_DICT[length]
                    return hash_input

                else:
                    self.retry('invalid hash')
            
            else:
                self.retry('invalid hash')
                    
                    
    def gen_wordlist(self,dictionary_name):
        # Prompts for a wordlist. If wordlist is not in the same directory as the program,
        # please enter the full path to the wordlist file.
        
        while self.user_file == None:
            self.filename = dictionary_name
            
            # If file exists, the self.user_file variable is set to the wordlist and the loop ends.
            try:
                self.user_file = open(self.filename, 'r', encoding='utf-8')
            
            # If the file does not exist, calls the retry method.
            except FileNotFoundError:
                self.retry('no file named '+self.filename)
        
        # Reads file and returns a list.
        words = self.user_file.read()
        self.user_file.close()
        return words.split()

    def dict_attack(self):
        # This method loops through the wordlist, converting each word to the hash type
        # and comparing the value to the hash entered by the user.
        # If/When the loop finds a match, the word is returned and the loop ends.
        # Also initializes the timer.
        self.start = time.time()
        print('Checking...\n\n')
        for word in self.wordlist:
            test = self.hashtype(word)
            if test == self.user_hash:
                return word
                
                
    def brute_force(self):
        # the brute force method. user enters required character set, min length and max length. 
        # the words are generated using itertools.product()
        charset = input('Please enter required character set: \n')
        minlen = int(input('Please enter minimum length: \n'))
        maxlen = int(input('Please enter maximum length: \n'))
        
        print('Checking...(this could take a while)\n\n')
        self.start = time.time()
        for i in range(minlen, maxlen+1):
            for p in product(charset, repeat=i):
                word = ''.join(p)
                print('word generated', word)
                if self.hashtype(word) == self.user_hash:
                    return word
                
                
    def retry(self, failure_type):
        # This method asks if another try is required. The method is used for invalid hash,
        # invalid wordlist and if the selected wordlist does not find a match.
        # The failure_type argument is a string.
        print('Sorry, '+failure_type+'. Would you like to try again? (y/n)')
        choice='a'
        while choice=='a':
            # If 'y' is selected, the loop ends and returns back to whichever method it was called from.
            # If 'n' is selected, the program ends.
            # If anything else is selected, the code returns to the beginning of the loop.
            choice = input()
            if choice.lower() == 'y':
                return
            elif choice.lower() == 'n':
                print('Thanks for using, goodbye.')
                sys.exit()
            else:
                choice='a'
                print('Invalid option. Please press y or n.')

def crack_hash_dictionary_attack(dictionary_name):
    run_it = Crackhash()
    run_it.dictionary_attack_call(dictionary_name)


def crack_hash_brute_force():
    run_it = Crackhash()
    run_it.brute_force_call()