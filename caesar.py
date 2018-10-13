alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y", "z"]
def encrypt_caesar(plaintext):
  ciphertext = ""
  for i in range(len(plaintext)):
     up = False
     if plaintext[i].isupper():
         up = True
     if plaintext[i].lower() in alphabet:
        if up:
         ciphertext += alphabet[(3 + alphabet.index(plaintext[i].lower())) % len(alphabet)].upper()
        else:
         ciphertext += alphabet[(3 + alphabet.index(plaintext[i])) % len(alphabet)]
  return ciphertext
print(encrypt_caesar("Python"))
def encrypt_decaesar(ciphertext):
    plaintext = ""
    for i in range(len(ciphertext)):
        up = False
        if ciphertext[i].isupper():
            up = True
        if ciphertext[i].lower() in alphabet:
            if up:
                plaintext += alphabet[((alphabet.index(ciphertext[i].lower()))-3) % len(alphabet)].upper()
            else:
                plaintext += alphabet[((alphabet.index(ciphertext[i].lower()))-3) % len(alphabet)]
    return plaintext
print(encrypt_decaesar("Sbwkrq"))