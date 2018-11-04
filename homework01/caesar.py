import string


def encrypt_caesar(plaintext: str) -> str:
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
    ciphertext = ""
    for i in range(len(plaintext)):
        up = False
        if plaintext[i].isupper():
            up = True
        if plaintext[i].lower() in string.ascii_lowercase:
            c = (3 + string.ascii_lowercase.index(plaintext[i].lower())) \
                % len(string.ascii_lowercase)
            if up:
                ciphertext += string.ascii_lowercase[c].upper()
            else:
                ciphertext += string.ascii_lowercase[c]
        else:
                ciphertext += plaintext[i]
    return ciphertext

def decrypt_caesar(ciphertext: str) -> str:
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
        plaintext = ""
        for i in range(len(ciphertext)):
            up = False
            if ciphertext[i].isupper():
                up = True
            if ciphertext[i].lower() in string.ascii_lowercase:
                c = ((string.ascii_lowercase.index(ciphertext[i].lower()))-3) \
                    % len(string.ascii_lowercase)
                if up:
                    plaintext += string.ascii_lowercase[c].upper()
                else:
                    plaintext += string.ascii_lowercase[c]
            else:
                    plaintext += ciphertext[i]
        return plaintext

