import base64

def encrypt_base64(text):
    #Tekst na bajty
    text_bytes = text.encode('utf-8')
    # Szyfrowanie za pomoca base64
    cryptogram = base64.b64encode(text_bytes)
    # Zwracanie szyfrowanego tekstu jako bajty
    return cryptogram.decode('utf-8')

# Test 
text =input ("podaj teskt do zaszyfrowania: ")
print("Tekst do zaszyfrowania:", text)
cryptogram = encrypt_base64(text)
print("Zaszyfrowany tekst:", cryptogram)
print("Odszyfrowany tekst:", base64.b64decode(cryptogram).decode('utf-8'))
