import random
import string

def generate_password_random(length=12):
    
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(alphabet) for _ in range(length))
    
    return password

print("Generated password (random):", generate_password_random(16))