from hashlib import sha256
import random
from secret import get_secret_key

SECRET_KEY = get_secret_key()

def generate_hash(password, app_name):
    salt = get_hex(SECRET_KEY, app_name)[:20]
    hsh = get_hex(salt, password)
    return ''.join((salt, hsh))
        
def get_hex(salt, password):
    return sha256((salt + password).encode('utf-8')).hexdigest()

def password(password, app_name, length):
    raw_hex = generate_hash(password, app_name)
    ALPHABET = ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTYVWXYZ', '0123456789', '(,._-*~"<>/|!@#$%^&)+=')

    chars = []

    while len(chars) < length:
        n = random.randint(0, len(ALPHABET)-1)
        alpha = ALPHABET[n]
        n = random.randint(0, len(alpha)-1)
        chars.append(alpha[n])

    return ''.join(chars)