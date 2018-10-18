def encrypt_caesar(plaintext:str)->str:
    """
        >>> encrypt_caesar("PYTHON")
        'SBWKRQ'
        >>> encrypt_caesar("python")
        'sbwkrq'
        >>> encrypt_caesar("Python3.6")
        'Sbwkrq3.6'
        >>> encrypt_caesar("")
        ''
        """
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
      else:
         ciphertext += plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext):
     """
        >>> decrypt_caesar("SBWKRQ")
        'PYTHON'
        >>> decrypt_caesar("sbwkrq")
        'python'
        >>> decrypt_caesar("Sbwkrq3.6")
        'Python3.6'
        >>> decrypt_caesar("")
        ''
         """
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
