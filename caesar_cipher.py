"""
    Logic:
        chr( (ord(txt[i]) + shift - 65)%26 + 65 )    
        The given character is comverted to its ascii code and shift is added which is then minus by start code of characters.
        The start code is minus so that we might know the offset fromt he original i.e. how much the given character is shifted from the start (65 or 97)
"""

def encrypt(txt:str, shift:int):
    """
    This method encrypts text by shifting the characters by the given shift.
    """

    res = ""
    for i in range(len(txt)):
        
        # Get ascii code of character
        c = ord(txt[i])
        if c >= 65 and c <= 90:
            res += chr( (c + shift - 65)%26 + 65 )

        elif c >= 97 and c <= 122:
            res += chr( (c + shift - 97)%26 + 97 )
    
    return res

def decrypt(txt:str, shift:int):
    """
    This method decrypts text by shifting the characters by the given shift.
    """

    res = ""
    for i in range(len(txt)):

        c = ord(txt[i])
        if c >= 65 and c <= 90:
            res += chr( (c - shift - 65)%26 + 65 )

        elif c >= 97 and c <= 122:
            res += chr( (c - shift - 97)%26 + 97 )
    
    return res

if __name__ == "__main__":
    text = "ATTACKATONCE"
    s = 3
    cipher = encrypt(text,s)
    print ("Text  : " + text)
    print ("Shift : " + str(s))
    print ("Cipher: " + cipher)
    print ("Decrypt: " + decrypt(cipher,s))