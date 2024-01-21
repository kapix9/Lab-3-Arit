import string
import random

def generate_password():
    # definicja znakow ktore moga zostac uzyte
    characters = string.ascii_letters + string.digits + string.punctuation
    # definicja dlugosci hasla od 8 do 16 znakow
    length_password = random.randint(8, 16)
    password = ''.join(random.choice(characters) for _ in range(length_password))
    return password

# test funkcji
print("Wygenerowane hasło:", generate_password())
