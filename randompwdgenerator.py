import random
import string

import secrets
import string

def generate_password(length=12):

    #Combines uppercase, lowercase, digits, and special symbols
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    #Builds password from a secure random selection of characters
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return password

def generate_strong_password(length=12):
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    
    while True:
        
        #generates random password with the characters from all_chars.
        password = ''.join(secrets.choice(all_chars) for _ in range(length))
        
        #checks for atleast one digit and atleast one symbol to be in the password
        if (any(c in digits for c in password)
                and any(c in symbols for c in password)):
            return password


#Generates a 16-character password.
print("Generated strong password:", generate_strong_password(16))