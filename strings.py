print('Understanding and using the strings with Python.'); 

# Double cote
print("\nPython is easy!")
print('I\'am developer.')
print('\nUsing the jump')
print(r'This string don\'t the escape' )
print('''
Python can used the string content 
In different lines
All the jump line is accepted...
''')
value = 10.5
print(f'The use of f before of string code allows to do a variable reference inside of string {value:.2f}')
print('Using the method fomat to do reference the a variable: {:.3f}'.format(value))

# Concat of strings and mutiply your content 
print('\n' + 5 * '---/---')
print('The dominian is called of: ' + 3 * 'w' + '.google.com')
print('\nConcat ' 'automaticaly ' ' with Python')

breack_long_strigs = ('\nThe Systax of Python is many interresant '
'like this is posible create differents types of strings')
print(breack_long_strigs.upper())

# Concat variables content and literals
literal = 'String '
print(literal + 'can to be concat join with a literal using the operator + ')

# Access te content such as a array 
word = 'Python'
print(word[0], word[5], word[-1], word[-3])

# Take the interval selected inside of a content
language = 'JavaScript'
print("Taking a interval inside of word:", language[4:10])
print("\nDifine others forms the create selections of content:", language[4:].upper() + ' or ' + language[:4].upper(), ' or still ', language[-1:].upper() )