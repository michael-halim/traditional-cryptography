"""
Caesar Cipher

Cn = PTn + key
Cn = Cipher Text
PT = Plain Text

"""
def main():
    text = input('Input Text : ')
    addition = int(input('Input Addition : '))

    while True:
        chc = input('Encrypt or Decrypt (0/1)')
        if chc in ['0','1']:
            break
        print('Choose 0 / 1')


    res = ''
    text = text.replace(' ','')
    addition = -addition if int(chc) else addition

    for character in text : 
        temp = ord(character) + addition
        if (character.isupper() and chr(temp) > 'Z') or (character.islower() and chr(temp) > 'z'):
            temp -= 26

        res += chr(temp)

    print(res)

if __name__ == '__main__':
    main()