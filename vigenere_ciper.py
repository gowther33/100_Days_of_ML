"""
Vigenere Cipher is a method of encryption that is a combination of multiple caesar ciphers. In Caesar cipher 
we shift every letter by 3 to get the cipher text. In Vigenere Cipher we use key to encrypt the message. The message is
called plain text. The encryption is done using the Vigenère table (tabula recta).

Approach:
The key letters are looked by row in the table and plain text letters are looked by column. The intersect of both gives the cipher text letters.
"""

def encipher(txt:str, key:str):
    res = ""
    n = len(txt)
    for i in range(n):
        # Plaintext int key
        pi = char_to_int(txt[i])
        # Key int key
        ki = char_to_int(key[i])
        # Cipher key
        ci = (pi + ki)%26 + 65    
        res += int_to_char(ci)
    return res


def decipher(txt:str, key:str):
    res = ""
    n = len(txt)
    for i in range(n):
        # Plaintext int key
        pi = char_to_int(txt[i])
        # Key int key
        ki = char_to_int(key[i])
        # Cipher key
        ci = (pi - ki)%26 + 65    
        res += int_to_char(ci)
    return res

def char_to_int(char:str):
    """ 
        Converts character to integer
    """
    index = ord(char)
    return index

def int_to_char(index):
    """
        Converts int to character
    """
    char = chr(index)
    return char


"""This function generates the key in a cyclic manner with length equal to
the length of original text. Cyclic manner means if the length of original text is greater then key then key's
characters are repeated
"""
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        diff = len(string) - len(key)
        print(f"Length Difference:{diff}")
        for i in range(diff):
            key.append(key[i % len(key)])
    return("" . join(key))


if __name__ == "__main__":
    string = "ATTACKATDAWN"
    keyword = "LEMON"
    key = generateKey(string, keyword)
    print(f"Key: {key}")
    cipher_text = encipher(string,key,)
    print("Original Text:", string)
    print("Ciphertext:", cipher_text)
    decipher_text = decipher(cipher_text,key,)
    print("Decrypted Text:", decipher_text)