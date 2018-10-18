def encrypt_caesar(plaintext):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
def encrypt_decaesar(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
        else:
            plaintext += ciphertext[i]
    return plaintext
