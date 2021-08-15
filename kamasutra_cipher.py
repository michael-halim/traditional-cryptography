import numpy as np
import random

"""
Random Array of ASCII Character
        ================================================
        array = ord('a') + np.arange(26).reshape((2,13))
        array = random_arr(array)
        ================================================

Fixed Array for Decrypting
        =======================================================================
        array = np.array([[ 98,108,105,107,97,102,103,100,104,109,106,101, 99],
                [111,121,118,120,110,115,116,113,117,122,119,114,112]])
        =======================================================================

Fixed Array of Character
        ==================================================================================================================
        array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random.shuffle(array) <-- optional
        array = [ord(character) for character in array]
        array = np.array(array).reshape((2,13))
        ==================================================================================================================
"""
def main():
        def random_arr(array):
                for i in range(random.randint(2,5)):
                        array[0] = np.roll(array[0],random.randint(1,13))
                        rng.shuffle(array,axis = 1)
                        array[1] = np.roll(array[1],random.randint(1,13))
                        rng.shuffle(array,axis = 0)

                return array

        rng = np.random.default_rng()

        array = np.array([[ 98,108,105,107,97,102,103,100,104,109,106,101, 99],
                        [111,121,118,120,110,115,116,113,117,122,119,114,112]])

        print(array)

        text = input('Input Text : ')
        text = text.replace(' ','')

        result = ''

        for character in text :   
                location = np.where(array == ord(character))    # Get the location of row and col from the array
                row , col = location[0][0] , location[1][0]     # Extract the row and col 
                new_row = 1 if row == 0 else 0                  # Reverse it , if the row 1 select 0 and vice versa
                result += chr(array[new_row][col])              # Assign the value to result

        print(result)

if __name__ == '__main__':
        main()