import base64

def szyfruj_base64(tekst):
    #Tekst na bajty
    tekst_bajty = tekst.encode('utf-8')
    # Szyfrowanie za pomoca base64
    szyfrogram = base64.b64encode(tekst_bajty)
    # Zwracanie szyfrowanego tekstu jako bajty
    return szyfrogram.decode('utf-8')

# Test 
tekst =input ("podaj teskt do zaszyfrowania: ")
print("Tekst do zaszyfrowania:", tekst)
szyfrogram = szyfruj_base64(tekst)
print("Zaszyfrowany tekst:", szyfrogram)
print("Odszyfrowany tekst:", base64.b64decode(szyfrogram).decode('utf-8'))
