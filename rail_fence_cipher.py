
"""
First element will be inserted directly then
There will be two passes through the matrix
pass 1: 1,2
pass 2: 1,0
loop will run len(msg) - 1
"""

print("********** Encryption ***********")
def encrypt(msg:str)-> str:
    _pass = 1 # 
    # First direct value
    mat[0][0] = msg[0]

    i = 0 # row
    j = 1 # col == len(msg)
    while (j < c):
        if _pass == 1:
            # go next row
            i+=1

            mat[i][j] = msg[j]
            
            # next column
            j+=1

            # pass change
            if i == 2:
                _pass = 2
        else:
            # 1 level up
            i-=1

            mat[i][j] = msg[j]
        
            # next col
            j+=1
        
            # pass change
            if i == 0:
                _pass = 1

    # Cipher text
    CT = ""
    for row in range(r):
        for col in range(c):
            if mat[row][col] == 0:
                continue
            else:
                CT = CT+mat[row][col]
    print(f"Cipher:{CT}")
    return CT


print("********** Decryption ***********")
def decrypt(msg:str)->str:
    # Decryption error
    _pass = 1 # 
    # First direct value
    mat[0][0] = CT[0]
    i = 0
    j = 1
    while (j < c):
        if _pass == 1:
            # go next row
            i+=1

            mat[i][j] = CT[j]
            
            # next column
            j+=1

            # pass change
            if i == 2:
                _pass = 2
        else:
            # 1 level up
            i-=1

            mat[i][j] = CT[j]
        
            # next col
            j+=1
        
            # pass change
            if i == 0:
                _pass = 1


    # Cipher text
    # Read the matrix diagonally
    PT = ""
    for row in range(r):
        for col in range(c):
            if row == col:
                PT = PT+mat[row][col]

    print(f"Plain Text:{PT}")
    return PT

def strip_(msg:str):
    new_msg = msg.replace(" ", "")
    return new_msg

if __name__ == "__main__":
    msg = "WONDERFUL"
    msg = strip_(msg)

    r = 3
    c = len(msg)
    mat = [[0 for i in range(c)] for j in range(r)]
    
    print(f"Message stripped:{msg}")
    cipher = encrypt(msg)
    print(f"Encrypted:{cipher}")
    _msg = decrypt(cipher)
    print(f"Decrypted:{_msg}")