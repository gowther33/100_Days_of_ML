import string

def generate_table(key):
    # Generate Playfair table from the given key
    key = key.upper().replace('J', 'I')
    alphabet = string.ascii_uppercase.replace('J', '')
    table = []
    for letter in key + alphabet:
        if letter not in table and letter != 'J':
            table.append(letter)
    playfair_table = [table[i:i+5] for i in range(0, 25, 5)]
    return playfair_table

def find_letter(table, letter):
    # Find the row and column of a given letter in the Playfair table
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                return i, j
    return None

def encrypt(plaintext, key):
    # Encrypt the plaintext using the Playfair Cipher
    playfair_table = generate_table(key)
    print(f"Table: {playfair_table}")
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    ciphertext = ''
    i = 0
    while i < len(plaintext):
        # Split the plaintext into pairs of letters
        pair = plaintext[i:i+2]
        if len(pair) == 1:
            pair += 'X'
        # Find the row and column of each letter in the pair
        row1, col1 = find_letter(playfair_table, pair[0])
        row2, col2 = find_letter(playfair_table, pair[1])
        if row1 == row2:
            # If the letters are in the same row, shift to the right
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            # If the letters are in the same column, shift down
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            # Otherwise, swap the columns of the two letters
            col1, col2 = col2, col1
        # Add the encrypted pair to the ciphertext
        ciphertext += playfair_table[row1][col1] + playfair_table[row2][col2]
        i += 2
    return ciphertext

def decrypt(ciphertext, key):
    # Decrypt the ciphertext using the Playfair Cipher
    playfair_table = generate_table(key)
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        # Split the ciphertext into pairs of letters
        pair = ciphertext[i:i+2]
        # Find the row and column of each letter in the pair
        row1, col1 = find_letter(playfair_table, pair[0])
        row2, col2 = find_letter(playfair_table, pair[1])
        if row1 == row2:
            # If the letters are in the same row, shift to the left
            col1 = (col1 - 1) % 5
            col2 = (col2 - 1) % 5
        elif col1 == col2:
            # If the letters are in the same column, shift up
            row1 = (row1 - 1) % 5
            row2 = (row2 - 1) % 5
        else:
            # Otherwise, swap the columns of the two letters
            col1, col2 = col2, col1
        # Add the decrypted pair to the plaintext
        plaintext += playfair_table[row1][col1]
    return plaintext


if __name__ == "__main__":
    key = "MONARCHY"
    PT = "ATTACK"
    cipher = encrypt(PT, key)
    print(f"Plaintext: {PT}")
    print(f"Cipher: {cipher}")