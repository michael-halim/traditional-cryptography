text = input('Input Text : ')
rows = int(input('Input Rows : '))
text = text.replace(' ','')

print(len(text))
arr = [ [] for x in range(rows)]
print(arr)
start = 0
state = 'incr'
state2 = 'allow'
for i in range(len(text)):
    pass