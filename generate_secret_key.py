import string
import random

def generate_secret_key():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.SystemRandom().choice(chars) for _ in range(50))

print('SECRET_KEY=',generate_secret_key())