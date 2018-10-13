alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y", "z"]
def encrypt_vigenere(plaintext, keyword):
 """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
 ciphertext = ''
 for i in range (len(plaintext) - len(keyword)):
     keyword += keyword[i]
 for j in range(len(plaintext)):
      up = False
      if plaintext[j].isupper():
          up = True
      if plaintext[j].lower() in alphabet:
          if up:
              ciphertext += alphabet[(alphabet.index(keyword[j].lower()) + alphabet.index(plaintext[j].lower())) % len(alphabet)].upper()
          else:
              ciphertext += alphabet[(alphabet.index(keyword[j].lower()) + alphabet.index(plaintext[j].lower())) % len(alphabet)]
 return ciphertext

def decrypt_vigenere(ciphertext, keyword):
"""
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
 plaintext = ''
 for i in range (len(ciphertext) - len(keyword)):
     keyword += keyword[i]
 for j in range(len(ciphertext)):
      up = False
      if ciphertext[j].isupper():
          up = True
      if ciphertext[j].lower() in alphabet:
          if up:
              plaintext += alphabet[(alphabet.index(ciphertext[j].lower()) - alphabet.index(keyword[j].lower())) % len(alphabet)].upper()
          else:
              plaintext += alphabet[(alphabet.index(ciphertext[j].lower()) - alphabet.index(keyword[j].lower())) % len(alphabet)]
 return plaintext
