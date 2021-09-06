import math
"""
    In Rail Fence Cipher, There's a problem when decrypting a text because there is a residue like this
    PT = I Like Cakes
    Row = 3
        I K A S
        L E K
        I C E

    CT = IKAS LEK ICE --> IKASLEKICE

    When we write IKASLEKICE back to decrypt we have to know where to divide the text into
    IKAS LEK ICE so we can work with it

    that's why i use the counter, the counter make sure it gets divided the same as we encrypt it

"""
def display_encrypted(arr):
    for row in arr:
        print (" ".join(map(str,row)) , end='')

def main():
        
    text = input('Input Text : ')
    rows = int(input('Input Rows : '))

    while True:
        chc = input('Encrypt or Decrypt (0/1)')
        if chc in ['0','1']:
            break
        print('Choose 0 / 1')

    text = text.replace(' ','')

    if int(chc):
        array = [ [] for i in range(rows)]   # Create Empty Array
        residue = len(text) % rows           # Calculate Residue from Division                   

        start = counter = 0                  

        for i in range(rows):  
            finish = start + len(text) // rows
            if counter < residue:
                finish = start + math.ceil( len(text) / rows )

            array[i].append(text[start : finish])
            start = finish
            counter += 1

        for i in range(rows):               # Change ['IKAS'] to ['I','K','A','S']
            array[i] = list(array[i][0])

        decrypted_text = ''
        col = 0

        for i in range(len(text)):
            if i % rows == 0 and i != 0:
                col += 1
            decrypted_text += array[i % rows][col]
            
        print(decrypted_text)

    else:
        array = []

        for i in range(rows):
            row = list()
            row.append(text[i::rows])       # Select ILIKECAKES with step of rows so that it slice at IKAS LEK ICE
            array.append(row)

        print(array)
        display_encrypted(array)

if __name__ == '__main__':
    main()