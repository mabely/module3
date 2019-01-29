# # Printing
# # New line
# print('Type something')
# something = input()

# # Space - no new line
# something = input('Type something: ')

# # Casting into int
# age = input('What is your age')
# age_int = int(age)

# # Casting to lowercase
# option = input('Please input yes or no: ').lower()

# ========================================================================
# Using len() to validate string length, without infinite loop

something = ''
while len(something) < 2 or len(something) > 15:
    try:
        something = input('Type something: ')
    except Exception as e:
        print(e)
    else:
        if len(something) < 2 or len(something) > 15:
            print('Please enter something between 2 - 15 characters')


# ========================================================================
# Using len() to validate string length, using infinite loop

while False:
    username = 'ada'
    try:
        while len(username) < 4 or len(username) > 12:
            username = input('Please choose a username: ')
            if len(username) < 4:
                print('Your username is too short! Min length is 4 characters.')
            elif len(username) > 12:
                print('Your username is too long! Max length is 12 characters.')
            else:
                print('Noted - thanks!')
        break
    except Exception as e:
        print('Something went wrong there',e)

## ========================================================================
while False:
    choice = 0
    try:
        while choice <1 or choice >3:
            choice = int(input('Make your choice: '))
            if choice <1 or choice >3:
                print('Please choose a number between 1 - 3!')
        break
    except ValueError:
        print('Enter a number please')

## ========================================================================
while False:
    print('*** Choices choices ***')
    print('1. Display my name')
    print('2. Display my age')
    print('3. Display my city')
    choice = 0
    try:
        while choice < 1 or choice > 3:
            # choice = int(input('Choose one of the options: '))

            choice = input('Choose one of the options: ')
            choice = int(choice)
            if choice < 1 or choice > 3:
                print('Please enter a number between 1 - 3')
            elif choice == 1:
                print('Mabel')
            elif choice == 2:
                print('29')
            elif choice == 3:
                print('London')
            else:
                print('That was unexpected, sorry something went wrong here...')
        break
    except ValueError:
        print('Please enter a number')

## ========================================================================
# Validation in classes

class Spam(object):
    def __init__(self, description, value):
        if not description or value >=0:
            raise ValueError
        self.description = description
        self.value = value
# here if there is nothing for descrip or value is 0 or more, then ValueError
s = Spam('meat', -1)
            
