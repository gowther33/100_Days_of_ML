import math

def encrypt(plaintext, key):
    # Remove spaces and convert the plaintext to uppercase
    plaintext = plaintext.replace(' ', '').upper()
    # Calculate the number of columns in the grid
    num_columns = len(key)
    # Pad the plaintext with trailing X's to fill the grid
    num_rows = int(math.ceil(len(plaintext) / float(num_columns)))
    plaintext += 'X' * (num_rows * num_columns - len(plaintext))
    # Generate the grid
    grid = []
    for i in range(num_rows):
        start = i * num_columns
        end = start + num_columns
        row = list(plaintext[start:end])
        grid.append(row)
    # Generate the ciphertext by reading the columns of the grid in the order given by the key
    ciphertext = ''
    key_order = sorted(range(num_columns), key=lambda k: key[k])
    print(key_order)
    for col in key_order:
        for row in grid:
            ciphertext += row[col]
    return ciphertext

def decrypt(ciphertext, key):
    # Calculate the number of columns in the grid
    num_columns = len(key)
    # Calculate the number of rows in the grid
    num_rows = int(math.ceil(len(ciphertext) / float(num_columns)))
    # Generate the grid
    grid = []
    for i in range(num_rows):
        start = i * num_columns
        end = start + num_columns
        row = list(ciphertext[start:end])
        grid.append(row)
    # Generate the plaintext by reading the rows of the grid in the order given by the key
    plaintext = ''
    key_order = sorted(range(num_columns), key=lambda k: key[k])
    for row in grid:
        for col in key_order:
            plaintext += row[col]
    # Remove any trailing X
    plaintext = plaintext.rstrip('X')
    return plaintext

if __name__ == "__main__":
    text = "We are discovered flee at once"
    key = "Zebras"
    cipher = encrypt(text,key)
    print ("Text  : " + text)
    print ("Cipher: " + cipher)
    msg = decrypt(cipher,key)
    print ("Decrypt: " + msg)