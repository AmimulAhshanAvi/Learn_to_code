color = 'blue'
guess = ''
guesses = 0

while guess != color:
    guess = input('what color am i thinking for? ')
    guesses = guesses + 1 

print('Yes, right ans.')
if guesses == 1:
 print('you need just one predict for the righ ans')
else:
 print('you need ', guesses ,'times to predict the right ans')
