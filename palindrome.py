ip_string = 'civil'
rev = ip_string[::-1]
if ip_string == rev:
    print(rev + 'is palindrome')
else:
    print(rev + ' is not palindrome')


##

string1 = input(('Enter a word:'))
if string1 == string1[::-1]:
    print('The word is palindrome')
else:
    print('The word is not a palindrome')

##

def pali_num(x):
    return x == x[::-1]
x = 'radar'
value = pali_num(x)
if value:
    print('Yes')
else:
    print('No')

