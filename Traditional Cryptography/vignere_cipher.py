"""
Vignere Cipher

Cn = (PTn + Kn) - 1 % 26
Cn = Cipher Text
PT = Plain Text
K = Key

How Vignere Cipher Works
PT = LASAGNA
K  = PASTA

Uneven length of key will be repeated so that it matches the plain text
L A S A G N A
P A S T A P A

Encrypting 
(( ASCII Text Number + ASCII Key Number - 2 * Subtraction ) % 26) + Subtraction

Subtraction is the base ASCII for lowercase letter
    the lowercase letter of `A` is 65 and `a` is 97

-2 * Subtraction is to make ASCII number become 26 letter digit in alphabet so that it can be % 26 without error
    then and only then that we add the subtraction again to return the ASCII to its original

In the formula there's -1 but in the code there isn't because of the indexing. In Real World `A` or `a` counts as 1 whereas 
    in code it counts as 0

Decrypting
((ASCII Text Number - ASCII Key Number + Addition) % 26 ) + Subtraction
Addition is to makes sure the ASCII number doesn't go bellow 0 by adding 26 if ASCII Text Number - ASCII Key Number < 0
    and just add 0 if it's above 0

% 26 is to makes sure after `z` or `Z` the alphabet goes back to `a` or `A`

The Subtraction is just to add the ASCII number back to its original

"""
def main():
    text = input('Input Text : ')
    key = input('Input Key : ')

    text = text.replace(' ','').lower()

    while True:
            chc = input('Encrypt or Decrypt (0/1)')
            if chc in ['0','1']:
                break
            print('Choose 0 / 1')

    if len(key) < len(text):                                    # Makes sure the Key is the same length as the Text
            times = len(text) // len(key)
            key = key * times + key[ : len(text) % len(key)]

    subtract = ord('a') if text.islower() else ord('A')         # Initialize the Subtraction (explained above)
    result = ''

    if int(chc):
        for i in range(len(text)):
            addition = 26 if ord(text[i]) - ord(key[i]) < 0 else 0
            result += chr((( ord(text[i]) - ord(key[i]) + addition  ) % 26 ) + subtract)

    else:
        for i in range(len(text)):
            result += chr((( ord(text[i]) + ord(key[i]) -  2 * subtract ) % 26 ) + subtract)

    print(result)

if __name__ == '__main__':
    main()