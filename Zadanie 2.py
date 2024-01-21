import string
import random

def generuj_haslo():
    # definicja znakow ktore moga zostac uzyte
    znaki = string.ascii_letters + string.digits + string.punctuation
    # definicja dlugosci hasla od 8 do 16 znakow
    dlugosc_hasla = random.randint(8, 16)
    haslo = ''.join(random.choice(znaki) for _ in range(dlugosc_hasla))
    return haslo

# test funkcji
print("Wygenerowane hasło:", generuj_haslo())
